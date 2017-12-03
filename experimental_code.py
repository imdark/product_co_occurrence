# records = [
# 	'ABDE',
# 	'BCE',
# 	'ABDE',
# 	'ABCE',
# 	'ABCDE',
# 	'BCD'
# ]


records = [
	'ABC',
]

# calculate frequency
char_frequency = {}


for record in records:
	for char in record:
		if char not in char_frequency:
			char_frequency[char] = 0
		char_frequency[char] += 1

# O(number_of_words * words_length * log(words_length))
sorted_records = [(sorted(record, reverse=True, key=lambda char: char_frequency[char])) for record in records]


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
			else:
				curr_node.children[value].frequency += 1

			curr_node = curr_node.children[value]

			if value in self.header and curr_node != self.header[value]:
				curr_node.next = self.header[value]
			
			self.header[value] = curr_node

	def get_conditional_paths(self):
		prefixes = []
		for value, header_node in self.header.items():

			curr_prefix = []
			while header_node is not None:
				curr_header_prefix = []
				curr_node = header_node.parent
				while curr_node.value is not None:
					curr_header_prefix.append(curr_node.value)
					curr_node = curr_node.parent
				
				# print('header_node', header_node.value, 'header_node.next', header_node.next)
				header_node = header_node.next
				curr_header_prefix.reverse()
				curr_prefix.append(curr_header_prefix)
			prefixes.append(curr_prefix)
		return prefixes


def build_prefix_tree(sorted_records):
	prefix_tree = FPTree()
	for record in sorted_records:
		prefix_tree.add(record)
	return prefix_tree

def get_frequencies_from_fp_tree(fp_tree):
	values_set = set()
	get_frequencies_from_fp_tree_dfs(fp_tree.root, '', values_set)

	return values_set

def get_frequencies_from_fp_tree_dfs(curr_node, curr_prefix, values_set):
	for child_value, child_node in curr_node.children.items():
		if (curr_prefix + child_value, child_node.frequency) not in values_set:
			values_set.add((curr_prefix + child_value, child_node.frequency))
			get_frequencies_from_fp_tree_dfs(child_node, curr_prefix + child_value, values_set)
			# to do this we need to create a new tree here with the frequncy of the sub patterns 
			# get_frequencies_from_fp_tree_dfs(child_node, child_value, values)


root_fp_tree = build_prefix_tree(sorted_records)
values = {}

def build_conditional_fp_trees(fp_tree, values):
	conditional_paths = fp_tree.get_conditional_paths()
	for path in conditional_paths:
		fp_tree = build_prefix_tree(path)
		frequencies = get_frequencies_from_fp_tree(fp_tree)
		print('frequencies', frequencies, 'path', path)
		
		for value, frequency in frequencies:
			values[value] = frequency
		
		build_conditional_fp_trees(fp_tree, values)

build_conditional_fp_trees(root_fp_tree, values)
# print(root_fp_tree.header, [node.value for node in root_fp_tree.header.values()])

print(values)