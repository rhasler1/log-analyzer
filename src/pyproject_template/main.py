import sys
import argparse
from .log_analyzer import analyze_log_static, analyze_log_dynamic

#TODO: 2/2/26-Think about moving size constraints from command line argument to a config file.

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
    parser.add_argument('-o', '--outputfilesize', type=int, 
                        help='the writable file\'s maximum size as bytes in decimal', default='4096')
    parser.add_argument('-b', '--buffersize', type=int,
                        help='the writable buffer\'s maximum size as bytes in decimal', default='4096')
    args = parser.parse_args()
    return args

def main() -> None:
    """This function is the main entry point to Log Analyzer.
    It gets command line arguments and sets program parameters.
    It asks the user to verify program parameters.
    If parameters are correct, proceeds to log analysis.
    Else, exits program.
    """
    args=parse_args()
    log_file=args.logfile
    pattern_file=args.patternfile
    output_file=args.outputfile
    output_file_size=args.outputfilesize
    buffer_size=args.buffersize

    try:
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
