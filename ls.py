#!/usr/bin/env python
import argparse
import os
import sys

def ls(path):
	files  = []
	for file in os.listdir(path):
		if file[0] != '.':
			files.append(file)
	sys.stdout.write('\n'.join(sorted(files)))

def ls_a(path):
	files = [os.curdir, os.pardir] + os.listdir(path)
	sys.stdout.write('\n'.join(sorted(files)))

def print_ls(args, func):
	if len(args.paths) > 1:
		for path in args.paths:
			sys.stdout.write(path + ':\n')
			func(path)
			if path != args.paths[-1]:
				sys.stdout.write('\n')
	else:
		func(args.paths[0])

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="print directory content")
	parser.add_argument('paths', nargs='*', type=str, default=['.'], help="path to directory")
	parser.add_argument('-a', '--all', action='store_false', help="show hidden files")
	args = parser.parse_args()

	if not args.all:
		print_ls(args, ls_a)
	else:
		print_ls(args, ls)
