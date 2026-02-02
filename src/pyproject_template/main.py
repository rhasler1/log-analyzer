import sys
import argparse
import logging
from .log_analyzer import analyze_log_static, analyze_log_dynamic
from .config import Config

logger = logging.getLogger(__name__)
def init_logger():
    """This function initializes the logger used by all
    project modules.
    """
    FORMAT = '%(asctime)s %(levelname)s %(message)s'
    logging.basicConfig(filename='log-analyzer.log', format=FORMAT, level=logging.INFO)

def parse_args():
    """This function parses positional and optional arguments.
    The positional arguments are required.

    Retval:
        args object
    """
    parser=argparse.ArgumentParser()
    parser.add_argument('logfile', type=str, help='path to logfile to analyze')
    parser.add_argument('patternfile', type=str, help='unstructured(no header) csv file with patterns to match against logfile')
    parser.add_argument('outputfile', type=str, help='path to output file to write results to')
    parser.add_argument('-d', '--dynamic', help='for dynamic log file analysis',
                        action='store_true')
    args = parser.parse_args()
    return args

def main() -> None:
    """This function is the main entry point to Log Analyzer.
    It gets command line arguments and sets program parameters.
    It asks the user to verify program parameters.
    If parameters are correct, proceeds to log analysis.
    Else, exits program.
    """
    init_logger()
    logger.info('In the program\'s main entry point')
    logger.info('Beginning to parse command line arguments')
    args=parse_args()
    log_file=args.logfile
    pattern_file=args.patternfile
    output_file=args.outputfile
    logger.info(f'Done parsing command line arguments. \
The log file path is set to \'{log_file}\'. \
The pattern file path is set to \'{pattern_file}\'. \
The output file path is set to \'{output_file}\'.')

    logger.info('Attempting to create configuration object')
    config=Config()
    if 'config' not in config.data:
        sys.exit(0)
    if ('buffer_size' not in config.data['config']
    or 'output_size' not in config.data['config']):
        sys.exit(0)
    buffer_size=int(config.data['config']['buffer_size'])
    output_file_size=int(config.data['config']['output_size'])
    logger.info(f'The configuraton object was successfully created. \
The internal buffer size is set to \'{buffer_size}\' Bytes. \
The output file size is set to \'{output_file_size}\' Bytes.')
   
    try:
        logger.info('Welcoming user and asking for parameter verification')
        print('\n- Welcome to Log Analyzer -')
        print('Press Ctrl+c to exit the program at anytime')
        print('\nThe command line positional and optional arguments have been parsed \
                \nPlease verify the following parameters:')
        print('\nPath to log file to analyze: {:s} \
                \nPath to pattern file to match against log file: {:s} \
                \nPath to output file to write results to: {:s} \
                \nthe output file\'s maximum size as bytes in decimal: {:d} \
                \nthe internal buffer\'s maximum size as bytes in decimal: {:d}'
              .format(log_file, pattern_file, output_file, output_file_size, buffer_size))
        
        user_input=input('\nAre these parameters correct? [yes]/[no] ')
        if user_input != 'yes':
            logger.info(f'User input \'{user_input}\' is not \'yes\' exiting program')
            print('\nProvide the desired parameters as positional and optional arguments when calling the program entry point')
            print('\nExiting program now')
            sys.exit(0)

        if args.dynamic:
            print('Starting dynamic analysis')
            analyze_log_dynamic(log_file, pattern_file, output_file)
        else:
            print('Starting static analysis')
            analyze_log_static(log_file, pattern_file, output_file)

    except KeyboardInterrupt:
        print("\nKeyboard Interrupt detected. Exiting gracefully.")
        sys.exit(0)

if __name__ == 'main':
    main()
