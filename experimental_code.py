# records = [
#     'ABDE',
#     'BCE',
#     'ABDE',
#     'ABCE',
#     'ABCDE',
#     'BCD'
# ]

records = [
	'ABC',
]

# records = [
# 	'AC',
# 	'AB',
# ]

# records = [
# 	'ACD',
# 	'AB',
# ]

# building a prefix tree O(number_of_words*avrage_words_length)
class FPNode(object):
	def __init__(self, value):
		self.value = value
		self.children = dict()
		self.frequency = 1
		self.next = None
		self.parent = None

class FPTree(object):
	def __init__(self):
		self.root = FPNode(None)
		self.header = {}

	def add(self, values):
		curr_node = self.root
		for value in values:
			if value not in curr_node.children:
				curr_node.children[value] = FPNode(value)
				curr_node.children[value].parent = curr_node

				if value in self.header:
					curr_node.children[value].next = self.header[value]
				self.header[value] = curr_node.children[value]
			else:
				curr_node.children[value].frequency += 1

			curr_node = curr_node.children[value]

def get_conditional_paths(tree):
	items = []

	for value, header_node in tree.header.items():
		start_node = header_node
		while start_node is not None:
			header_suffix = []
			parent_node = start_node
			while parent_node.value is not None:
				header_suffix.append(parent_node)
				parent_node = parent_node.parent
			items.append((value, header_suffix))
			start_node = start_node.next
	return items

def get_frequencies_from_fp_tree(tree, suffix = []):
	item_paths = get_conditional_paths(tree)
    for item, path in item_paths:
    	if item not in suffix:
            found_set = [item] + suffix
            yield found_set, sum(node.frequency for node in path)
            cond_tree = FPTree()
            cond_tree.add(list(node.value for node in path))
            for record in get_frequencies_from_fp_tree(cond_tree, found_set):
            	yield record

def build_prefix_tree(sorted_records):
	prefix_tree = FPTree()
	for record in sorted_records:
		prefix_tree.add(record)
	return prefix_tree


# calculate frequency
char_frequency = {}

for record in records:
	for char in record:
		if char not in char_frequency:
			char_frequency[char] = 0
		char_frequency[char] += 1

# O(number_of_words * words_length * log(words_length))
sorted_records = [(sorted(record, reverse=True, key=lambda char: char_frequency[char])) for record in records]

root_fp_tree = build_prefix_tree(sorted_records)
# get_conditional_paths(root_fp_tree)

list(get_frequencies_from_fp_tree(root_fp_tree, suffix = []))