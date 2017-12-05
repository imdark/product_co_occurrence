import sys
import argparse
from collections import namedtuple
from frequent_item_sets.fp_growth import get_members_cooccernces

def parse_args():
	parser = argparse.ArgumentParser(description='Find corelated transactions.')
	parser.add_argument(
	    '-i', '--input-path', metavar='input path', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
	    help='''
	    Input super marked co-location of products file path, file in the format, <sku 1 id >, <sku 2 id>, …. <sku N id> (default: stdin).
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

def read_transactions(input_file):
	'''
	'''
	print('started reading input')
	line = input_file.readline()
	while line is not '':
		# remove break lines
		yield line.strip().split(TRANSACTION_SPLITTER)
		line = input_file.readline()
	print('finished reading input')



def write_cooccurrences(cooccurrences, output_file):
	pass

MIN_SET_SIZE = 3

def get_product_cooccurrence(transactions, min_support = 0):
	''' pydoc
	'''
	members_cooccernces = get_members_cooccernces(transactions, min_support)

	members_cooccernces_of_min_size = \
		[ProductsCoOccurrence(members_coocernce, frequency) for members_coocernce, frequency in members_cooccernces \
		if len(members_coocernce) > MIN_SET_SIZE]
	return members_cooccernces_of_min_size

def main():
	input_path, output_path, min_support = parse_args()
	transactions = read_transactions(input_path)
	product_cooccurrences = get_product_cooccurrence(list(transactions), min_support)
	for product_cooccurrence in product_cooccurrences:
		print(product_cooccurrence)

if __name__ == '__main__':
	main()