#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 MiguelHeCa <josemiguel@heca.tech>
#
# Distributed under terms of the MIT license.

"""
Functional Tests
"""
import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_todo_list(self):
        self.browser.get('http://localhost:8000')
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main()
