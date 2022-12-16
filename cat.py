#!/usr/bin/env python
import argparse
import sys


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="cat command")
	parser.add_argument('files', nargs='+', default=sys.stdin, help='paths to files')
	args = parser.parse_args()
	
	for file in args.files:
		with open(file) as content:
			sys.stdout.write(content.read())