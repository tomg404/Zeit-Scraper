from pathlib import Path


basedir = Path().absolute()

XML_DIR = str(basedir.joinpath('xml-temp/'))
SAVE_XML_DIR = str(basedir.joinpath('xml-files/'))
CSV_FILE = str(basedir.joinpath('data.csv'))
DELIMITER = '|'
FIELDNAMES = ['author', 'title_length', 'subtitle_length',
            'genre', 'ressort', 'sub_ressort', 'edited',
            'corrected', 'copyrights', 'comments', 'text_length',
            'color_scheme', 'date_first_released', 'tags', 'title',
            'subtitle', 'location']

# notify.run config
USE_NOTIFY = False
ENDPOINT = 'https://notify.run/XXXXXXXXXX'
