
#Using linkedlist
from LinkedList import LList

class Stack:

	def __init__(self):
		self.stack=LList()

	def push(self,val):
		self.stack.addLast(val)

	def peek(self):
		return self.stack.tail.val

	def pop(self):
		return self.stack.removeLast()

	def size(self):
		return self.stack.size()


#Using Arrays
class Stack1():

	def __init__(self):
		self.stack=[]

	def push(self,val):
		self.stack.append(val)

	def pop(self):
		assert(len(self.stack))
		return self.stack.pop()

	def peek(self):
		assert(len(self.stack))
		return self.stack[-1]

	def size(self):
		return len(self.stack)

	def isEmpty(self):
		return self.size()==0



#Using collections.deque.....For Large N

from collections import deque

class Stack2():

	def __init__(self):
		self.stack=deque()

	def push(self,val):
		self.stack.append(val)

	def pop(self):
		assert(len(self.stack))
		return self.stack.pop()

	def peek(self):
		assert(len(self.stack))
		return self.stack[-1]

	def size(self):
		return len(self.stack)

	def isEmpty(self):
		return self.size()==0


if __name__=='__main__':
	s=Stack()
	s.push(6)
	print(s.pop())
	#print(s.isEmpty())
	s.push(5)
	s.push(9)
	print(s.peek())
	print(s.size())
