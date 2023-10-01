#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 MiguelHeCa <josemiguel@heca.tech>
#
# Distributed under terms of the MIT license.

"""
Functional Tests
"""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert "Congratulations!" in browser.title
print("OK")
