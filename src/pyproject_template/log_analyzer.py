# This module is in a broken state.
# TODO: Fix 2/2/26

import os.path
from datetime import datetime
import itertools

class LogAnalyzer:
    # Setting class attributes
    # 1 MB file limit
    _MAX_LOG_FILE_SIZE_BYTES=(1024 * 1024)
    
    # Correspond to the size of the data analyzed
    _CHUNK_SIZE=1024

    @property
    def MAX_LOG_FILE_SIZE_BYTES(self):
        return self._MAX_LOG_FILE_SIZE_BYTES

    # Magic method
    def __init__(self, log_file: str, flags=[''], starting_position=0):
        # Validating method parameters
        if not os.path.isfile(log_file):
            raise ValueError('Log file: {:s} could not be found'.format(log_file))

        with open(log_file, 'r') as file:
            line_count=0
            current_size=0
            for line in file:
                current_size += len(line.encode('utf-8'))
                if (current_size > self._MAX_LOG_FILE_SIZE_BYTES):
                    raise ValueError('The file size: {:d} surpasses \
                                     max file size: {:d}'.format(current_size, self._MAX_LOG_FILE_SIZE_MB))
                line_count+=1
       
        if starting_position >= line_count:
            raise ValueError(f'Starting position: {starting_position} (starting position) \
                    is out of bounds: {line_count} (line count)')

        # Setting instance attributes
        self._logs_processed_total=0
        self._logs_flagged_total=0
        # Flagged log store
        self._logs_flagged=[]
        # Flags to check against log entries
        self._flags=flags
        # Correspond to the number of lines to skip before analyzing
        self._starting_position=starting_position
        self._log_file=log_file
   

        with open(log_file, 'r') as file:
            line_count=0
            current_size=0
            for line in file:
                current_size += len(line.encode('utf-8'))
                if (current_size > self._MAX_LOG_FILE_SIZE_BYTES):
                    raise ValueError('The file size: {:d} surpasses \
                                     max file size: {:d}'.format(current_size, self._MAX_LOG_FILE_SIZE_MB))
                line_count+=1
       

    def run_adv(self):
        """This function
        """
        with open(self._log_file, 'r') as log_file:
            for entry in log_file:
                current_size += len(entry.encode('utf-8'))
                if (current_size > self._MAX_LOG_ANALYZER_MEM_BYTES):
                    # Stop reading in data
                    break;


    @property
    def logs_processed_total(self):
        """This function returns the value of instance
                attribute _logs_processed_total as a property.
                It is safe to return this value directly because `int`
                is immutable.
        """
        return self._logs_processed_total

    @property
    def logs_flagged_total(self):
        """This function returns the value of instance
                attribute _logs_flagged_total as a property.
        """
        return self._logs_flagged_total

    @property
    def logs_flagged(self):
        """This function creates and returns a tuple whose elements are
                references to the instance attribute _logs_flagged
                elements. _logs_flagged elements are immutable string
                objects. This means the caller cannot mutate the instance's
                state using this property.
        """
        return tuple(self._logs_flagged)
    
    @property
    def flags(self):
        """This function creates and returns a tuple whose elements are
                references to the instance attribute _flags
                elements. _flags elements are immutable string
                objects. This means the caller cannot mutate the instance's
                state using this property.
        """
        return tuple(self._flags)

    @property
    def starting_position(self):
        """This function returns the value of instance
                attribute _starting_position as a property.
                It is safe to return this value directly because `int` 
                is immutable
        """
        return self._starting_position

    @property
    def log_file(self):
        """This function returns the value of instance
                attribute _log_file as a property.
                It is safe to return this value directly because `str`
                is immutable
        """
        return self._log_file

    def run_adv(self):
        """
        """
        while (1):
            with open(self._log_file, 'r') as log:
                log_trimmed = itertools.islice(
                        log,
                        (self._starting_position+self._logs_processed_total),
                        None
                        )

                for entry in log_trimmed:
                    for flag in self._flags:
                        if flag in entry:
                            self._logs_flagged_total+=1
                            self._logs_flagged.append(entry)

                    self._logs_processed_total+=1

    def run(self):
        """This instance method starts the LogAnalyzer
        Note: Logs flagged total can be more than the number
        of entries in the log file if multiple flags are
        found in a single entry. Flagged logs are also appended to the
        _logs_flagged container multiple times for same reason.
        """
        with open(self._log_file, 'r') as log:
            for entry in log:
                for flag in self._flags:
                    if flag in entry:
                        self._logs_flagged_total+=1
                        self._logs_flagged.append(entry)

                self._logs_processed_total+=1

def analyze_log_static(log_file, pattern_file, output_file) -> None:
    print('This module is in a broken state, returning.')
    #log_analyzer = LogAnalyzer(log_file, pattern_file, output_file, output_file_size, buffer_size)

def analyze_log_dynamic(log_file, pattern_file, output_file) -> None:
    print('This module is in a broken state, returning.')

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
