#Singly Linked List

class Node:
	def __init__(self,val):
		self.val=val
		self.next=None
class LList:
	def __init__(self):
		self.head=None
		self.tail=None
		self.len=0

	def size(self):
		return self.len

	def isEmpty(self):
		return self.size()==0

	def print(self):
		if not self.isEmpty():
			temp=self.head
			while(temp):
				print(temp.val,end=' ')
				temp=temp.next
			print('\n')

	def addFront(self,val):
		new_node=Node(val)
		if self.isEmpty():
			self.head=self.tail=new_node
		else:
			new_node.next=self.head
			self.head=new_node
		self.len+=1

	def addLast(self,val):
		new_node=Node(val)
		if self.isEmpty():
			self.head=self.tail=new_node
		else:
			self.tail.next=new_node
			self.tail=new_node
		self.len+=1

	#def insert(self,val,pos):

	def removeFirst(self):
		assert(self.size())
		self.head=self.head.next
		self.len-=1
		if self.isEmpty():
			self.head=None
			self.tail=None

	def removeLast(self):
		assert(self.size())
		if self.head==self.tail:
			data=self.head.val
			self.removeFirst()
			self.head=None
			self.tail=None
		else:
			data=self.tail.val
			v=self.head
			while(v.next!=self.tail):
				v=v.next
			v.next=None
			self.tail=v
		return data


if __name__=="__main__":
	llist=LList()
	llist.addFront(9)
	llist.addFront(0)
	llist.addFront(1)
	llist.addFront(2)
	llist.addFront(5)
	llist.addFront(7)
	llist.print()
	print(llist.tail.val)
	print(llist.head.val)
	print(llist.size())
	llist.removeFirst()
	print(llist.removeLast())
	llist.print()
	print(llist.size())


