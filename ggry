#!/usr/bin/env python
#vim: fileencoding=utf-8

from __future__ import print_function, division, unicode_literals
import argparse
import urllib
import webbrowser


def parse_args():
    description = "Google search from command line."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("words", help="search words")
    parser.add_argument("--browser", "-b", help="specify browser")
    return parser.parse_args()


def build_url(words):
    template = "http://google.com/search?q={0}"
    quoted = urllib.quote_plus(words)
    return template.format(quoted)


def get_controller(browser):
    browser_name = browser if browser is not None else ""
    return webbrowser.get(browser_name)


if __name__ == "__main__":
    args = parse_args()
    url = build_url(args.words)
    controller = get_controller(args.browser)
    controller.open(url)
