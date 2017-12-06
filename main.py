from collections import namedtuple
from frequent_item_sets.fp_growth import get_members_cooccernces, Transaction
from typing import *
from io_manager import *


ProductsCoOccurrence = namedtuple('ProductsCoOccurrence', ['products_set', 'co_occurrence_frequency'])

MIN_SET_SIZE = 3

def get_product_cooccurrence(transactions : List[Transaction], min_support : int = 0):
	members_cooccernces = get_members_cooccernces(transactions, min_support)

	members_cooccernces_of_min_size = \
		[ProductsCoOccurrence(members_coocernce, frequency) for members_coocernce, frequency in members_cooccernces \
		if len(members_coocernce) > MIN_SET_SIZE]

	return members_cooccernces_of_min_size

def main():
	input_path, output_path, min_support = parse_commandline_args()
	transactions = read_transactions(input_path)
	product_cooccurrences = get_product_cooccurrence(list(transactions), min_support)
	write_cooccurrences(product_cooccurrences, output_path)

if __name__ == '__main__':
	main()