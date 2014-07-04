#!/usr/bin/python
# -*- coding: utf-8 -*-


import cPickle
import htmlparser
import urllib2
from collections import deque


class Monitor(object):
    """monitor web resource by compare local records and remote url"""

    def __init__(self, url, localfile, tag_list):
        self.url = url
        self.file = localfile
        self.tag_list = tag_list

    def dump_to_file(self):
        """save content to local file"""
        with open(self.file, 'w') as fp:
            cPickle.dump(self.retrieve_web_list(), fp)

    def retrieve_local_list(self):
        """read build list from local file"""
        local_list = []
        with open(self.file, 'r') as fp:
            local_list = cPickle.load(fp)
        return local_list

    def retrieve_web_list(self):
        """retrieve list from web"""
        web_list = []
        req = urllib2.urlopen(self.url)
        seed = req.read()
        req.close()
        parser = htmlparser.MyHTMLParser()
        parser.feed(seed)
        web_list = [url for url in parser.urls if url.startswith(self.tag_list)]
        parser.close()
        return deque(web_list)

    def new_list(self):
        """get new list by compare web list and local list"""
        return list(set(self.retrieve_web_list()) - set(self.retrieve_local_list()))
