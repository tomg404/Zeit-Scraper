#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from time import strftime, gmtime, time
import traceback
from src.vars import *
import src.writer as writer
import src.scraper as scraper
import src.cleaner as cleaner
import src.argparser as argparser
import src.downloader as downloader



if __name__ == '__main__':
    csv_file = str(CSV_FILE)
    xml_dir = str(XML_DIR)
    save_xml_dir = str(SAVE_XML_DIR)
    try:
        argparser.parse()

        # creates new csv file if it doesn't already exist
        if not os.path.isfile(csv_file):
            writer.create_new(csv_file)

        if not os.path.exists(xml_dir):
            os.makedirs(xml_dir)

        if not os.path.exists(save_xml_dir):
            os.makedirs(save_xml_dir)

        print('---------%s---------' % strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        start_time = time()
        downloader.download()
        scraper.main()
        cleaner.clean()
        print('Execution took %s seconds' % (round(time() - start_time, 3)))
        print('-------------------------------------')

    except Exception as e:
        error_msg = 'Something went horribly wrong. Please check the program.\nError: %s' % e
        print(error_msg)
        traceback.print_exc()
        # if USE_NOTIFY is True it sends a message to the given endpoint
        if USE_NOTIFIER:
            from pushnotifier import PushNotifier as pn
            from threading import Thread
            def send_notification():
                PN.send_text(error_msg)
            Thread(target=send_notification).start()
