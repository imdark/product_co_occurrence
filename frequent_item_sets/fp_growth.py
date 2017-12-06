from typing import *
from frequent_item_sets.fp_tree import FPTree
from collections import namedtuple

Transaction = namedtuple('Transaction', ['transaction_ids'])

def sort_transactions_by_member_frequency(transactions : List[Transaction]):
	'''
	To allow creating the FP Tree in a consistent way from multiple transactions, we sort every transaction by the frequncy of its skus
	'''
	
	print('started sorting transactions')
	# calculate frequency per sku_id
	sku_id_frequency = {}

	for transaction in transactions:
		for sku_id in transaction:
			if sku_id not in sku_id_frequency:
				sku_id_frequency[sku_id] = 0
			sku_id_frequency[sku_id] += 1

	# O(number_of_transactions * transactions_length * log(transactions_length))
	# sort transaction by frequency per sku_id
	sorted_transactions = [(sorted(transaction, reverse=True, key=lambda sku_id: sku_id_frequency[sku_id])) for transaction in transactions]
	print('finished sorting transactions')


	return sorted_transactions


def get_conditional_pattern_base(fp_tree : FPTree):
	'''
	For every sku in the tree, we group all the transactions that end with this sku.
	This allows us to create an fp_tree per sku
	'''
	conditional_pattern_base = []
	for key, start_node in fp_tree.header.items():
		next_node = start_node
		curr_paths = []

		# traverse fp_tree right
		while next_node is not None:
			curr_node = next_node.parent
			path_to_start_node = []
			# traverse fp_tree up
			while curr_node.value is not None:
				path_to_start_node.append(curr_node.value)
				curr_node = curr_node.parent
			path_to_start_node.reverse()
			curr_paths.append((path_to_start_node, next_node.frequency))
			next_node = next_node.next
		conditional_pattern_base.append((key, curr_paths))
	return conditional_pattern_base

def get_members_cooccernces_from_fp_tree(fp_tree : FPTree, min_support  : int = 0, suffix : List[str] = []):
	'''
	we recursivly create an frequent_pattern_tree per every sku-cooccored-sku combination, 
	it allows us to return all frequncies
	'''
	conditional_pattern_base = get_conditional_pattern_base(fp_tree)

	for key, conditional_pattern in conditional_pattern_base:
		if key not in suffix:
			fp_tree = FPTree()
			curr_sum = 0
			for prefix, frequency in conditional_pattern:
				fp_tree.add(prefix, frequency)
				curr_sum += frequency
			if curr_sum >= min_support:
				yield (suffix + [key], curr_sum)
				for result in get_members_cooccernces_from_fp_tree(fp_tree, min_support, suffix + [key]):
					yield result

def get_members_cooccernces(transactions : List[Transaction], min_support : int = 0):
	'''
	We create a combined frequnct pattern tree from all the transactions, and then recursively prune the tree
	creating a pattern for each subtree based on its parent tree
	'''
	sorted_transactions = sort_transactions_by_member_frequency(transactions)
	fp_tree = FPTree()
	for transaction in sorted_transactions:
		fp_tree.add(transaction)
	return get_members_cooccernces_from_fp_tree(fp_tree, min_support)
