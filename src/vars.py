from pathlib import Path


basedir = Path().absolute()

XML_DIR = basedir / 'xml-temp/'
SAVE_XML_DIR = basedir / 'xml-files/'
CSV_FILE = basedir / 'data.csv'
DELIMITER = '|'
FIELDNAMES = ['author', 'title_length', 'subtitle_length',
            'genre', 'ressort', 'sub_ressort', 'edited',
            'corrected', 'copyrights', 'comments', 'text_length',
            'color_scheme', 'date_first_released', 'tags', 'title',
            'subtitle', 'location']

# notify.run config
USE_NOTIFY = False
ENDPOINT = 'https://notify.run/XXXXXXXXXX'