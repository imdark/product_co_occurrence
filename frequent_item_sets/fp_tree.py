from typing import *

class FPNode(object):
	def __init__(self, value : str, frequency : int = 1):
		self.value = value
		self.children = dict()
		self.frequency = frequency
		self.next = None
		self.parent = None

class FPTree(object):
	'''
	FP tree is a trie like data stracture containing an extra field for how many times
	a specific pattern was added to the tree on the node representing the last member of that sequunce 
	'''
	def __init__(self):
		self.root = FPNode(None)
		self.header = {}

	def add(self, values : List[str], frequency : int = 1):
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