from datetime import datetime
import argparse

# Project entry point
def main() -> None:
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-file", type=str, required=True)
    args = parser.parse_args()
    log_file = args.log_file
    print(f'log file = {log_file}')

    log(log_file, 'Starting main script')
    log(log_file, 'Begin function foo in main')
    foo()
    log(log_file, 'End function foo in main')
    log(log_file, 'Exiting main script')

def foo() -> None:
    print('Hello world!')

def log(logfile: str, message: str) -> None:
    """This function writes the message 'message' and time of occurrence into the file logfile.

    Args:
        logfile (str): log file
        message (str): message to be written into the log file
    """
    # datetime format. Remark that:
    ## .%f appends the parts of the second
    ## the tailing ', ' are intentionally used to separate the timestamp and the logged message
    datatime_format = '%Y-%m-%d-%H:%M:%S.%f, '
    datetimestamp = datetime.now().strftime(datatime_format)

    ## log events are separated by the new character
    with open(logfile, 'a') as file:
        file.write(datetimestamp + message + '\n')
