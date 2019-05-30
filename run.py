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


if __name__ == '__main__':
    argparser.argparser()
    try:
        # creates new csv file if it doesn't already exist
        if not os.path.isfile(CSV_FILE):
            writer.create_new(CSV_FILE)

        if not os.path.exists(XML_DIR):
            os.makedirs(XML_DIR)

        if not os.path.exists(SAVE_XML_DIR):
            os.makedirs(SAVE_XML_DIR)

        start_time = time.time()
        downloader.download()
        scraper.main()
        cleaner.clean()
        print("-Execution took %s seconds" % (round(time.time() - start_time, 3)))

    except Exception as e:
        error_msg = 'Something went horribly wrong. Please check the program.\nError: %s' % e
        print(error_msg)

        # send the error via notify.run if USE_NOTIFY is True
        if USE_NOTIFY:
            from notify_run import Notify
            from threading import Thread
            def send_notification():
                notify = Notify()
                notify.send(error_msg, ENDPOINT)
            Thread(target=send_notification).start()
