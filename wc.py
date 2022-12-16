#!/usr/bin/env python
import argparse
import sys

def wc(*files):
	results = {}
	for file in files:
		chars, words, lines = 0, 0, 0
		with open(file, 'r') as f:
			for line in f:
				lines += 1
				words += len(line.split())
				chars += len(line)
		results[file] = { 'lines': lines, 'words': words, 'chars': chars}
	return results

def wc_out(files, option = None):
	if not option:
		total = {'lines': 0, 'words': 0, 'chars': 0}
		for file in files:
			sys.stdout.write(str(files[file]['lines']) + '\t' + str(files[file]['words']) + '\t' + str(files[file]['chars']) + '\t' + file + '\n')
			for key in ['lines', 'words', 'chars']:
				total[key] += files[file][key]
		sys.stdout.write(str(total['lines']) + '\t' + str(total['words']) + '\t' + str(total['chars']) + '\t' + 'total' + '\n')
	else:
		total = 0
		for file in files:
			sys.stdout.write(str(files[file][option]) + '\t' + file + '\n')
			total += files[file][option]
		sys.stdout.write(str(total) + '\t' + 'total' + '\n')

if __name__ == '__main__':
	options = {'-l':'lines', '-w':'words', '-c':'chars'}
	parser = argparse.ArgumentParser(description="Count lines, words, and bytes for a file")
	
	for option in options:
		parser.add_argument(option, action='append', type=str, nargs='+', help='number of ' + options[option])
	
	parser.add_argument("files", action='append', type=str, nargs="*", help="paths to files")
	args = parser.parse_args()
	
	if args.files[0] != []:
		wc_out(wc(*args.files[0]))
	if args.l:
		wc_out(wc(*args.l[0]), 'lines')
	if args.w:
		wc_out(wc(*args.w[0]), 'words')
	if args.c:
		wc_out(wc(*args.c[0]), 'chars')