import csv

def unstructuredcsv_to_frozenset(csv_file: str):
    """This function parses an unstructured csv file placing
    each value into a mutable set.

    Data Cleaning:
        Values containing only whitespace are filtered out of the set.
    
        Values with leading and trailing whitespace are normalized by
        stripping the leading and trailing whitespace.

    Immutable Copy:
        An immutable frozenset is created with the values in the mutable set 
        after data cleaning.

    Exception From File Operation:
        An empty immutable set is returned.

    Retval:
        The frozenset
    """
    retval=set()
    try:
        with open(csv_file) as file:
            csv_reader=csv.reader(file, delimiter=',')
            rows_matrix=[]
            for row in csv_reader:
                for value in row:
                    retval.add(value)
    except FileNotFoundError:
        print(f'File \'{csv_file}\' could not be found')
    except PermissionError:
        print(f'File \'{csv_file}\' could not be opened \
                because of inadequate access rights.')
    
    # In Python an empty string resolves to false. So the following
    # statement reads as "If this value in the set is not empty after
    # stripping whitespace, then retain the value and strip whitespace."
    retval = {value.strip() for value in retval if value.strip()} 
    return frozenset(retval)
