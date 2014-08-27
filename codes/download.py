#!/usr/bin/env python
"""
    Download all files from a page with specify suffix
    Usage:
        ./download.py -u http://xxxx.com/page -s pdf
"""

import urllib
import urllib2
import subprocess as sp
import argparse
from HTMLParser import HTMLParser
from multiprocessing import Process


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
    _args = parser.parse_args()
    return _args


def worker(src, des):
    urllib.urlretrieve(src, des)


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
            jobs = []
            for p in parser.urls:
                if p.endswith(suffix):
                    process = Process(target=worker, args=(url+p, p))
                    jobs.append(process)
                    process.start()
                    #sp.call(['wget', url + p])
    elif url.startswith('ftp'):
        f = urllib2.urlopen(url).read()
        for line in f.split('\n'):
            p = line.split()[len(line.split()) - 1]
            sp.call(['wget', url + p])
    else:
        pass


if __name__ == "__main__":
    args = parse_options()
    download_url = args.url
    download_suffix = args.suffix.split(',')
    retrieve(download_url, tuple(download_suffix))
