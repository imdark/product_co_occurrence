import sys
import argparse
from collections import namedtuple
from frequent_item_sets.fp_growth import Transaction
from typing import *
import io

def parse_commandline_args():
	parser = argparse.ArgumentParser(description='Find corelated transactions.')
	parser.add_argument(
	    '-i', '--input-path', metavar='input path', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
	    help='''
	    Input super markd co-location of products file path, file in the format, <sku 1 id >, <sku 2 id>, …. <sku N id> (default: stdin).
	    ''')
	parser.add_argument(
	    '-o', '--output-path', metavar='output path', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
	    help='''
	    Output co-appered frequency, in the format: <sku set size (N)>, <co-occurrence frequency>, <sku 1 id >, <sku 2 id>, …. <sku N id> (default: stdout).
	    ''')
	parser.add_argument(
	    '-s', '--min-support', type=int, metavar='int', nargs='?', default=4,
	    help='Minimum sigma, support ratio, times that elements appered togather (must be > 0, default: 4).')

	args = parser.parse_args()
	return args.input_path, args.output_path, args.min_support


Arguments = namedtuple('Arguments', ['input_path', 'output_path', 'min_support'])
ProductsCoOccurrence = namedtuple('ProductsCoOccurrence', ['products_set', 'co_occurrence_frequency'])

TRANSACTION_SPLITTER = ' '

def read_transactions(input_file : io.IOBase):
	'''
		Read input file transactions in the format <sku 1 id >, <sku 2 id>, …. <sku N id> 
	'''
	print('started reading input')
	line = input_file.readline()
	while line is not '':
		# remove break lines and spaces
		yield line.strip().split(TRANSACTION_SPLITTER)
		line = input_file.readline()
	print('finished reading input')



def write_cooccurrences(cooccurrences : List[ProductsCoOccurrence], output_file : io.IOBase):
	'''
		write transactions to file in the format:
		<item set size (N)>, <co-occurrence frequency>, <item 1 id >, <item 2 id>, …. <item N id>
	'''
	for cooccurrence in cooccurrences:
		output_file.write('{:d}, {:d}, {:s}\n'.format(
			len(cooccurrence.products_set), cooccurrence.co_occurrence_frequency, ', '.join(cooccurrence.products_set)))
