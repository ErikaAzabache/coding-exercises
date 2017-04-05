class Node(object):
	"""Node in a linked list"""

	def __intit__ (self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	"""Linked list"""

	def __init__ (self):
		self.head = None
		self.tail = None

	def print_list(self):
		"""printing aall elements in the list"""

		current = self.head
		while current is not None:
			print current.data
			current = current.next
	def find(self, data):
		"""finding data in the linked list"""
		current = head
		while current is not None:
			if current.data == data:
				return True
		return False
	def append(self, data):
		"""append a node with data to the end of the list"""
		new_node = Node(data)

		if (self.head is None) and (self.tail is None):
			self.head = new_node

		if self.tail is not None:
			self.tail.next = new_node

		self.tail = new_node

	def remove_by_value(self, data):
		pass

	def remove_by_index(self, idx):
		pass

	def insert_by_index(self, idx):
		pass

	


