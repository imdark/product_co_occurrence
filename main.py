import sys
import argparse
from collections import namedtuple

def parse_args():
	parser = argparse.ArgumentParser(description='Find corelated transactions.')
	parser.add_argument(
	    '-i', '--input-path', metavar='input path', nargs='?', type=argparse.FileType('r'), default=[sys.stdin],
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


	return parser.parse_args()

args = parse_args()
print(args.input_path, args.output_path, args.min_support)

ProductsCoOccurrence = namedtuple('products_set', 'co_occurrence_frequency')

MIN_SET_SIZE = 3
def get_product_cooccurrence():
	''' pydoc
	'''
