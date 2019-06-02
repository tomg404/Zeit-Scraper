# -*- coding: utf-8 -*- 

import argparse as ap

__version__ = "1.1"
__author__ = "Tom Gaimann | github.com/tomg404"

def argparser():
    parser = ap.ArgumentParser(description="""
    Project for downloading and scraping all new articles from https://www.zeit.de.\n
    Please see the vars.py file (src/vars.py) if you want to use the service of https://notify.run.\n""",
    epilog="(c) %s" % __author__)
    parser.add_argument('-v', '--version', action='version', version="Version: %s" % __version__, help="show program's version number and exit")
    parser.add_argument('-o', '--output-file', help="set the ouput file path") # TODO: make this work
    parser.add_argument('-n', '--enable-notify', action='store_true') # TODO: make this work
    parser.add_argument('-e', '--set-notify-endpoint') # TODO: make this work too
    args = parser.parse_args()

# idea : put argparse in run.py
#        code a method in vars.py to change the values
#        call the method from vars.py in run.py and pass the values from argparse in the function
