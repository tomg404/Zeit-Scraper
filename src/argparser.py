import argparse as ap
from . import __version__, __author__


def parse():
    parser = ap.ArgumentParser(description="""
    Project for downloading and scraping all new articles from https://www.zeit.de""",
    epilog="(c) %s" % __author__)
    parser.add_argument('-v', '--version', action='version', version="Version: %s" % __version__, help="show program's version number and exit")
    parser.add_argument('-e', '--enable-pushnotifier', action='store_true', help='Enable PushNotifier')
    # parser.add_argument('-o', '--output-file', help="set the ouput file path") # TODO: make this work
    args = parser.parse_args()
    return args
