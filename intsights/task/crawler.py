class Crawler(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def crawl(self):
        yield self.base_url

