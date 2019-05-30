# Scrapes articles in xml-temp and moves them to xml-files to store them (forever)
import os
from pathlib import Path
import src.writer as writer
from src.vars import XML_DIR, SAVE_XML_DIR, USE_NOTIFY, ENDPOINT
import xml.etree.ElementTree as ET


# defines a article object which contains the scraped data
class Article:
    def __init__(self, location):
        self.location = location
        self.url = 'http://'    # TODO: fix this
        self.author = None
        self.title = None
        self.title_length = None
        self.subtitle = None
        self.subtitle_length = None
        self.genre = None
        self.ressort = None
        self.sub_ressort = None
        self.edited = None
        self.corrected = None
        self.copyrights = None
        self.comments = None
        self.text_length = None
        self.color_scheme = None
        self.date_first_released = None
        self.tags = []

    def scrape(self):
        tree = ET.parse(self.location)
        root = tree.getroot()

        # search in <head>
        head = root.find('head')
        for attribute in head.findall('attribute'):
            if attribute.get('name') == 'title':
                self.title = attribute.text
            if attribute.get('name') == 'author':
                self.author = attribute.text
            if attribute.get('name') == 'ressort':
                self.ressort = attribute.text
            if attribute.get('name') == 'sub_ressort':
                self.sub_ressort = attribute.text
            if attribute.get('name') == 'genre':
                self.genre = attribute.text
            if attribute.get('name') == 'edited':
                self.edited = attribute.text
            if attribute.get('name') == 'corrected':
                self.corrected = attribute.text
            if attribute.get('name') == 'copyrights':
                self.copyrights = attribute.text
            if attribute.get('name') == 'comments':
                self.comments = attribute.text
            if attribute.get('name') == 'color_scheme':
                self.color_scheme = attribute.text
            if attribute.get('name') == 'date_first_released':
                self.date_first_released = attribute.text
            if attribute.get('name') == 'text-length':
                self.text_length = attribute.text

        rankedTags = head.find('rankedTags')
        for tag in rankedTags.findall('tag'):
            self.tags.append(tag.text)

        # searches <body> for title and super title
        body = root.find('body')
        try:
            self.title = body.find('title').text
            self.title_length = len(self.title)
        except:
            pass
        ###
        try:
            self.subtitle = body.find('subtitle').text
            self.subtitle_length = len(self.subtitle)
        except:
            pass



def main():
    counter = 0
    fail_counter = 0

    for file in os.listdir(str(XML_DIR)):
        try:
            a = Article(str(XML_DIR.joinpath(file)))
            a.scrape()

            dict = {
            'location': str(a.location),
            'author': str(a.author),
            'title': str(a.title),
            'title_length': str(a.title_length),
            'subtitle': str(a.subtitle),
            'subtitle_length': str(a.subtitle_length),
            'genre': str(a.genre),
            'ressort': str(a.ressort),
            'sub_ressort': str(a.sub_ressort),
            'edited': str(a.edited),
            'corrected': str(a.corrected),
            'text_length': str(a.text_length),
            'copyrights': str(a.copyrights),
            'comments': str(a.comments),
            'color_scheme': str(a.color_scheme),
            'date_first_released': str(a.date_first_released),
            'tags': str(a.tags),
            }
            writer.insert_data(dict)

            counter += 1    # increment success counter
            os.rename(str(XML_DIR.joinpath(file)), str(SAVE_XML_DIR.joinpath(file))) # move the files to the storage

        except Exception as e:
            print('Error: ', e)
            fail_counter += 1   # increment fail counter

    result_msg = '-Scraped %s new article(s). %s failed.' % (counter, fail_counter)
    print(result_msg)

    # if USE_NOTIFY is True it sends a message to the given endpoint
    if USE_NOTIFY:
        from notify_run import Notify
        from threading import Thread
        def send_notification():
            notify = Notify()
            notify.send(result_msg, ENDPOINT)
        Thread(target=send_notification).start()
