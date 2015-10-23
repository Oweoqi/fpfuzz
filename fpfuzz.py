#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import sys
import argparse

parser = argparse.ArgumentParser(description='Simple as heck URL fuzzer')
parser.add_argument('-i', action="store", required=True, dest="payload")
parser.add_argument('-u', action="store", required=True, dest="url")
parser.add_argument('-v', action="version", version="%(prog)s 0.1")

script_input = parser.parse_args()

f = open(script_input.payload, 'r')
r = requests.get(script_input.url)

for line in f:
	print r.status_code,
	print script_input.site + line

f.close()

