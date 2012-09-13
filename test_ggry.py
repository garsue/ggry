#!/usr/bin/env python
#vim: fileencoding=utf-8

from __future__ import print_function, division, unicode_literals
import unittest
import argparse

import ggry


class TestGtty(unittest.TestCase):
    def test_arg(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("words", nargs="+")
        parser.add_argument("--browser", "-b")
        test = parser.parse_args("spam ham egg -b w3m".split())
        self.assertEqual(test.words, ["spam", "ham", "egg"])
        self.assertEqual(test.browser, "w3m")
        test = parser.parse_args("spam ham egg".split())
        self.assertEqual(test.words, ["spam", "ham", "egg"])
        self.assertIsNone(test.browser)

    def test_build_url(self):
        expect = "http://google.com/search?q=spam+%2B+ham"
        test = ggry.build_url(["spam", "+", "ham"])
        self.assertEqual(test, expect)
