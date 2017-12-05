from frequent_item_sets.fp_tree import FPTree


def get_members_cooccernces(records):
	sorted_records = sort_records_by_member_frequency(records)
	fp_tree = FPTree()
	
	for record in sorted_records:
		fp_tree.add(record)
	
	return get_records_sequnces(fp_tree)

def get_records_sequnces(fp_tree, suffix = []):
	conditional_pattern_base = get_conditional_pattern_base(fp_tree)

	for key, conditional_pattern in conditional_pattern_base:
		if key not in suffix:
			fp_tree = FPTree()
			curr_sum = 0
			for prefix, frequency in conditional_pattern:
				fp_tree.add(prefix)
				curr_sum += frequency
			yield ([key] + suffix, curr_sum)
			
			get_records_sequnces(fp_tree, [key] + suffix)

def sort_records_by_member_frequency(records):
	# calculate frequency
	char_frequency = {}

	for record in records:
		for char in record:
			if char not in char_frequency:
				char_frequency[char] = 0
			char_frequency[char] += 1

	# O(number_of_words * words_length * log(words_length))
	sorted_records = [(sorted(record, reverse=True, key=lambda char: char_frequency[char])) for record in records]

	return sorted_records


def get_conditional_pattern_base(fp_tree):
	conditional_pattern_base = []
	for key, start_node in fp_tree.header.items():
		next_node = start_node
		curr_paths = []
		while next_node is not None:
			curr_node = next_node
			path_to_start_node = []
			while curr_node.value is not None:
				path_to_start_node.append(curr_node.value)
				curr_node = curr_node.parent
			path_to_start_node.reverse()
			curr_paths.append((path_to_start_node, next_node.frequency))
			next_node = start_node.next
		conditional_pattern_base.append((key, curr_paths))
	return conditional_pattern_base