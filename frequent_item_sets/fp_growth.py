from frequent_item_sets.fp_tree import FPTree

def sort_records_by_member_frequency(records):
	# calculate frequency per char
	char_frequency = {}

	for record in records:
		for char in record:
			if char not in char_frequency:
				char_frequency[char] = 0
			char_frequency[char] += 1

	# O(number_of_transactions * transactions_length * log(transactions_length))
	# sort transaction by frequency per char
	sorted_records = [(sorted(record, reverse=True, key=lambda char: char_frequency[char])) for record in records]

	return sorted_records


def get_conditional_pattern_base(fp_tree):
	'''
	For every sku in the tree, we group all the transactions that end with this sku.
	This allows us to create an fp_tree per sku
	'''
	conditional_pattern_base = []
	for key, start_node in fp_tree.header.items():
		print('fp_tree.header.items()', fp_tree.header.items())
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
			next_node = start_node.next
		conditional_pattern_base.append((key, curr_paths))
	return conditional_pattern_base

def get_members_cooccernces_from_fp_tree(fp_tree, min_support = 0, suffix = []):
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

def get_members_cooccernces(records, min_support = 0):
	sorted_records = sort_records_by_member_frequency(records)
	fp_tree = FPTree()
	for record in sorted_records:
		fp_tree.add(record)
	return get_members_cooccernces_from_fp_tree(fp_tree, min_support)
