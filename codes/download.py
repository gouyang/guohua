#!/usr/bin/python
"""Download from a page with specified suffix"""

import urllib2
import subprocess as sp
import argparse
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def reset(self):
        HTMLParser.reset(self)
        self.urls = []

    def handle_starttag(self, tag, attrs):
        href = [v for k, v in attrs if k == 'href']
        if href:
            self.urls.extend(href)


def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="url of the resource")
    parser.add_argument("-s", "--suffix", help="target's suffix")
    args = parser.parse_args()
    return args

def retrieve(url, suffix):
    if url.startswith('http'):
        parser = MyHTMLParser()
        if not url.endswith('/'):
            url = url + '/'
        f = urllib2.urlopen(url)
        if f.code == 200:
            parser.feed(f.read())
            f.close()
            parser.close()
            for p in parser.urls:
                if p.endswith(suffix):
                    sp.call(['wget', url + p])
    elif url.startswith('ftp'):
        f = urllib2.urlopen(url).read()
        for line in f.split('\n'):
            p = line.split()[len(line.split()) - 1]
            sp.call(['wget', url + p])
    else:
        pass


if __name__ == "__main__":
    args = parse_options()
    url = args.url
    suffix = args.suffix.split(',')
    retrieve(url, tuple(suffix))
