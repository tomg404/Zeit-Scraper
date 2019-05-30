#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.vars import CSV_FILE, XML_DIR, SAVE_XML_DIR, USE_NOTIFY, ENDPOINT
import src.downloader as downloader
import src.scraper as scraper
import src.cleaner as cleaner
import src.writer as writer
import src.argparser as argparser
import time
import os
import traceback


if __name__ == '__main__':
    csv_file = str(CSV_FILE)
    xml_dir = str(XML_DIR)
    save_xml_dir = str(SAVE_XML_DIR)
    argparser.argparser()
    try:
        # creates new csv file if it doesn't already exist
        if not os.path.isfile(csv_file):
            writer.create_new(csv_file)

        if not os.path.exists(xml_dir):
            os.makedirs(xml_dir)

        if not os.path.exists(save_xml_dir):
            os.makedirs(save_xml_dir)

        start_time = time.time()
        downloader.download()
        scraper.main()
        cleaner.clean()
        print("-Execution took %s seconds" % (round(time.time() - start_time, 3)))

    except Exception as e:
        error_msg = 'Something went horribly wrong. Please check the program.\nError: %s' % e
        print(error_msg)
        traceback.print_exc()

        # send the error via notify.run if USE_NOTIFY is True
        if USE_NOTIFY:
            from notify_run import Notify
            from threading import Thread
            def send_notification():
                notify = Notify()
                notify.send(error_msg, ENDPOINT)
            Thread(target=send_notification).start()
