#!/usr/bin/env python
import argparse
import sys

if __name__ == '__main__':
	lines = []
	parser = argparse.ArgumentParser(description="Sort lines of text files")
	parser.add_argument('files', nargs='+', help="paths to files")
	args = parser.parse_args()
		
	for file in args.files:
		with open(file, 'r') as file:
			for line in file:
				lines.append(line)
			if lines[-1][-1] != '\n':
				lines[-1] += '\n'

	for line in sorted(lines):
		sys.stdout.write(line)