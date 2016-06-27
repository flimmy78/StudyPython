#! /usr/bin/env python3.3
# -*- coding: GB2312 -*-
'''
Created on 2016-5-26

@author: LiuHao
'''
import sys
import importlib
import argparse

def main(argv):
    print(importlib.import_module('__main__').__doc__.split("\n")[1]);

    parser = argparse.ArgumentParser(description="description",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     argument_default=argparse.SUPPRESS)
    parser.add_argument("-r", "--recursive", dest="recurse", action="store_true", help="recurse into subfolders [default: %(default)s]")
    parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
    parser.add_argument("-i", "--include", dest="include", help="only include paths matching this regex pattern. Note: exclude is given preference over include. [default: %(default)s]", metavar="RE" )
    parser.add_argument("-e", "--exclude", dest="exclude", help="exclude paths matching this regex pattern. [default: %(default)s]", metavar="RE" )
    parser.add_argument('-V', '--version', action='version', version="1.0")
    parser.add_argument(dest="paths", help="paths to folder(s) with source file(s) [default: %(default)s]", nargs='+')

    args = parser.parse_args(argv[1:])
    if "include" in args:
        print(args.include)
    print(args)

if __name__ == '__main__':
    sys.argv.append("-v");
    sys.argv.append("-r");
    sys.argv.append("-iabcd");
    sys.argv.append("dddd")
    sys.argv.append("cccc")
    sys.exit(main(sys.argv))