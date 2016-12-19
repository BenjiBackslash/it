from .utils import Utils
import time
import threading
from .paste_scraper import PasteScraper
from .crawler import Crawler
from .db import DB


class Runner:
    def __init__(self):
        self.db = DB()
        self.base_crawler_url = 'http://nzxj65x32vh2fkhk.onion/all'

    def run(self, sleep_minutes):
        while True:
            crawler = Crawler(self.base_crawler_url)
            for url in crawler.crawl():
                self.ProcessUrlThread(url, PasteScraper(self.db)).start()
            time.sleep(sleep_minutes*60)

    class ProcessUrlThread(threading.Thread):
        def __init__(self, url, scraper):
            self.url = url
            self.scraper = scraper

        def run(self):
            html_text = Utils.download_html_text(self.url)
            self.scraper.scrape(html_text)

