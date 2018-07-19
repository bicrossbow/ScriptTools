# download url to local path

# encoding: utf-8
"""
url_download.py

Created by Nu on 2018-07-8
"""

import sys
import getopt #C-style parser for command line options
import os

help_message = """
options:
    -h, --help  show the help message
    -u          input path
    -o          output path
"""

def main(argv=None):
    if argv == None:
        argv = sys.argv # get arguments from terminal

    # init internal variables
    url = None
    output_path = None
    file_name = None

    # get system arguemnts
    try:
        optlist, args = getopt.getopt(argv[1:],'hu:o:f:')
    except getopt.GetoptError as err:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)

    # option processing
    #print(optlist)
    #print(args)
    for option, value in optlist:
        if option in ('-h','--help'):
            print(help_message)
            sys.exit(0)
        if option in ('-u'):
            url = value
        if option in ('-o'):
            output_path = value

    print('url={}'.format(url))
    print('output_path={}'.format(output_path))

    # check input args
    #assert(url)
    if url==None:
        print('URL is not specified')
        sys.exit(2)
    if output_path is None:
        print('path is not specified')
        output_path = os.getcwd()
        print('use current path:{}'.format(output_path))
    elif not os.path.exists(output_path):
        print('path does not exist:{}\n Abort!'.format(output_path))
        sys.exit(2)
    

    #processing.....
    print('Link: {link}'.format(link=url))
    print('Path: {path}'.format(path=output_path))

    os.chdir(output_path)

    command = 'curl -O {link}'.format(link=url)
    return os.system(command)

if __name__ == "__main__":
    sys.exit(main())