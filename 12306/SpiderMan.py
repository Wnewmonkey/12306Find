from docopt import docopt

from Get_Address import Get_Address
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser


class SpiderMan(object):


    def __init__(self):
        self.address = Get_Address()
        self.download = HtmlDownloader()
        self.parser = HtmlParser()
    def crawl(self):
        info = self.address.get_address()
        html_lists = self.download.download(info)
        tickets = self.parser.parser(html_lists)



if __name__ == "__main__":
    SpiderMan().crawl()
