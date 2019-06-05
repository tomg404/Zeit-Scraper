from pathlib import Path
from pushnotifier import PushNotifier as pn

basedir = Path().absolute()

XML_DIR = basedir.joinpath('xml-temp/')
SAVE_XML_DIR = basedir.joinpath('xml-files/')
CSV_FILE = basedir.joinpath('data.csv')
DELIMITER = '|'
FIELDNAMES = ['author', 'title_length', 'subtitle_length',
            'genre', 'ressort', 'sub_ressort', 'edited',
            'corrected', 'copyrights', 'comments', 'text_length',
            'color_scheme', 'date_first_released', 'tags', 'title',
            'subtitle', 'location']

# pushnotifier.de config
USE_NOTIFIER = True
if USE_NOTIFIER:
    #                      user,  pass, package, api_key
    PN = pn.PushNotifier('XXXX', 'XXXX', 'XXXX', 'XXXX')
