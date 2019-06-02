### Downloads the xml file of every new article on zeit.de in a folder
import random
from pathlib import Path
import os
import requests
import xml.etree.ElementTree as ET
from src.vars import XML_DIR, SAVE_XML_DIR

xml_file = str(XML_DIR.joinpath('index.xml'))

# url where every new article on the frontpage is listed
xml_index_url = 'http://xml.zeit.de/index'

def main():
    r = requests.get(xml_index_url).text
    with open(xml_file, 'w') as xml:
        xml.write(r)
    articles = get_all_article_urls(xml_file)
    download_all_articles(articles)

# get all urls out of (index)xml file
def get_all_article_urls(xml_file):
    url_array = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    blocks = root.iter('block')
    for data in blocks:
        # check if data is an article
        if(data.get('contenttype') == 'article'):
            xml_url = data.get('href')
            url_array.append(xml_url)
    return url_array

# downloads all articles in url_array and checks if they already exist
def download_all_articles(urls_array):
    new_file_counter = 0
    failed_file_counter = 0
    for i in range(0, len(urls_array)):
        filename = urls_array[i].split('/')[-1] + '.xml'    # splits the url at '/' and takes only the name
        download_destination = str(XML_DIR.joinpath(filename))
        temp_dir = str(SAVE_XML_DIR.joinpath(filename))
        # checks if file already exists in temp directory or in the storage
        # directory. if not .. DOWNLOAD!
        if os.path.isfile(download_destination):
            pass
        elif os.path.isfile(temp_dir):
            pass
        else:
            try:
                r = requests.get(urls_array[i]).text
                with open(download_destination, 'w') as d:
                    d.write(r)

                new_file_counter += 1
            except:
                failed_file_counter += 1

    print('-Downloaded %s new files! %s failed.' % (new_file_counter, failed_file_counter))

def download():
    try:
        main()
        os.remove(xml_file) # delete the index xml file
    except Exception as e:
        print('Error: ', e)
        print('Something went wrong in %s!' % __file__)
