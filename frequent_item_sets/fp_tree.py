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
				child_node = FPNode(value, frequency)
				child_node.parent = curr_node

				# if there is already a node in for this value, connect to the existing node, and create a linked list
				if value in self.header:
					child_node.next = self.header[value]
				self.header[value] = child_node
				curr_node.children[value] = child_node
			else:
				curr_node.children[value].frequency += frequency
			
			curr_node = curr_node.children[value]