#!/usr/bin/env python
import argparse
import shutil
import os
import sys

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="remove file/directory")
	parser.add_argument('paths', nargs='+', default=sys.stdin, type=str, help="path to file")
	parser.add_argument('-r', '--recursive', action='store_true', help='recursively remove directory')
	args = parser.parse_args() 

	for path in args.paths:
		if os.path.isfile(path):
			os.remove(path)
		elif os.path.isdir(path):
			if args.recursive:
				shutil.rmtree(path)
			else:
				sys.stdout.write('cannot remove ' + path + ': Is a directory\n')
		else:
			sys.stdout.write("No such file or directory\n")