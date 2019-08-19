#!/usr/bin/python3

import os, sys
try:
	path = str(sys.argv[1])
	print(len(os.listdir(path)))
except IndexError:
	print(len(os.listdir()))

