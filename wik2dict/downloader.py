#!/usr/bin/env python

import urllib2
import os


def download(wiki = "wp", language = "wo"):
    """Download MediaWiki XML dump."""

    #todo: support 7z
    if wiki == "wp":
        file = language + "wiki-latest-pages-meta-history.xml.bz2"
        url = "http://download.wikimedia.org/" + language + "wiki/latest/" + file

    f_url_in = urllib2.urlopen(url)
    if not os.path.exists("dumps"):
        os.mkdir("dumps")

    f_out = open(os.path.join("dumps", file), 'w')
    f_out.writelines(f_url_in.readlines())


if __name__ == "__main__":
    download()

