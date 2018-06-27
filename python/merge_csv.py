# Script to merger csv under one folder to a single csv file

# encoding: utf-8
"""
merge_csv.py

Created by Nu on 2018-06-25
"""

import sys
import getopt #C-style parser for command line options
import os
import time
import csv

help_message = """
options:
    -h, --help  show the help message
    -i          input path
    -o          output path
optional:
    -t          csv_prefix,
                default to process all csv files
                specity prefix to merge csv starts with specific string
"""

def main(argv=None):
    if argv == None:
        argv = sys.argv # get arguments from terminal

    start_time = time.time()    # record time at the beginning of processing
    # init internal variables
    input_path = None
    output_path = None
    csv_prefix = ''

    # get system arguemnts
    try:
        optlist, args = getopt.getopt(argv[1:],'hi:o:t:')
    except getopt.GetoptError as err:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)

    # option processing
    print(optlist)
    print(args)
    for option, value in optlist:
        if option in ('-h','--help'):
            print(help_message)
            sys.exit(0)
        if option in ('-i'):
            input_path = value
        if option in ('-o'):
            output_path = value
        if option in ('-t') and len(value)>0:
            csv_prefix = value

    print('input_path={}'.format(input_path))
    print('output_path={}'.format(output_path))
    print('csv_prefix={}'.format(csv_prefix))

    # check input args
    assert(input_path)
    if input_path==None:
        print('input path is not specified')
        sys.exit(2)
    if not os.path.exists(input_path):
        print('path not exist:{}'.format(input_path))
        sys.exit(2)
    

    #processing.....

    end_time = time.time()      # record time at the end of processing
    print('~~~~~ Processing time: {:.2f} seconds ~~~~~'.format(end_time-start_time))

if __name__ == '__main__':
    main()