import configparser
from pathlib import Path
from pushnotifier import PushNotifier as pn
import src.argparser as ap


# file paths
basedir = Path().absolute()
XML_DIR = basedir.joinpath('xml-temp/')
SAVE_XML_DIR = basedir.joinpath('xml-files/')
CSV_FILE = basedir.joinpath('data.csv')
CONFIG_FILE = basedir.joinpath('config.ini')

# csv variables
DELIMITER = '|'
FIELDNAMES = ['author', 'title_length', 'subtitle_length',
            'genre', 'ressort', 'sub_ressort', 'edited',
            'corrected', 'copyrights', 'comments', 'text_length',
            'color_scheme', 'date_first_released', 'tags', 'title',
            'subtitle', 'location']

# pushnotifier.de config
USE_NOTIFIER = ap.parse().enable_pushnotifier
if USE_NOTIFIER:
    def import_login_data(config_path):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(str(config_path))
        data = ['user','pass','package','apikey']
        data[0] = config['PushNotifier']['Username']
        data[1] = config['PushNotifier']['Password']
        data[2] = config['PushNotifier']['PackageName']
        data[3] = config['PushNotifier']['ApiKey']
        return data
    data = import_login_data(CONFIG_FILE)
    PN = pn.PushNotifier(data[0], data[1], data[2], data[3])
