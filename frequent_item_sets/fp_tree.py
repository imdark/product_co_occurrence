class FPNode(object):
	def __init__(self, value, frequency = 1):
		self.value = value
		self.children = dict()
		self.frequency = frequency
		self.next = None
		self.parent = None

class FPTree(object):
	def __init__(self):
		self.root = FPNode(None)
		self.header = {}

	def add(self, values, frequency = 1):
		'''
		Add a Transaction to the tree, allows for adding the same transaction multiple times using the frequency parameter
		'''
		curr_node = self.root
		for value in values:
			if value not in curr_node.children:
				curr_node.children[value] = FPNode(value, frequency)
				curr_node.children[value].parent = curr_node
				if value in self.header:
					curr_node.children[value].next = self.header[value]
				self.header[value] = curr_node.children[value]
			else:
				curr_node.children[value].frequency += frequency
			
			curr_node = curr_node.children[value]
		# print('add', values, frequency, self.header['A'].next)
