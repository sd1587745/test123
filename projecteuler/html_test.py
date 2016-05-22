__author__ = 'X'
from html.parser import HTMLParser
import urllib.request

url = 'https://www.python.org/events/python-events/'
page = urllib.request.urlopen(url)


class MyHtmlParser(HTMLParser):
    def __init__(self):
        super(MyHtmlParser,self).__init__()
        self.event = []
        self.date = []
        self.datetmp = []
        self.location = []
        self.eventtrig = False
        self.datetrig = False
        self.locationtrig = False

    def handle_starttag(self, tag, attrs):
        if tag == 'h3':
            for key, value in attrs:
                if value == 'event-title':
                    self.eventtrig = True
        if tag == 'time':
            for key, value in attrs:
                if key == 'datetime':
                    self.datetrig = True
        if tag == 'span':
            for key, value in attrs:
                if key == 'class' and value == 'event-location':
                    self.locationtrig = True

    def handle_data(self, data):
        if self.eventtrig:
            self.event.append(data)
        if self.datetrig:
            self.datetmp.append(data)
        if self.locationtrig:
            self.location.append(data)
            print(data)

    def handle_endtag(self, tag):

        if tag == 'a':
            self.eventtrig = False
        if tag == 'time':
            self.datetrig = False
            self.date.append('-'.join(self.datetmp))
            self.datetmp = []
        if tag == 'span':
            self.locationtrig = False

parser = MyHtmlParser()
parser.feed((page.read().decode('GBK')))

for x in range(0, 8):
    print(parser.event[x]+'\n'+parser.location[x]+'\n'+parser.date[x]+'\n'*3)



