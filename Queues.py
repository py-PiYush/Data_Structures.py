#using Arrays

class Queue():

	def __init__(self):
		self.queue=[]

	def enqueue(self,val):
		self.queue.append(val)

	def dequeue(self):
		assert(len(self.queue))
		return self.queue.pop(0)

	def front(self):
		assert(len(self.queue))
		return self.queue[0]

	def rear(self):
		assert(len(self.queue))
		return self.queue[-1]

	def size(self):
		return len(self.queue)

	def isEmpty(self):
		return self.size()==0


#Using collections.deque.....faster
from collections import deque

class Queue1():
	def __init__(self):
		self.queue=deque()

	def enqueue(self,val):
		self.queue.append(val)

	def dequeue(self):
		assert(len(self.queue))
		return self.queue.popleft()

	def size(self):
		return len(self.queue)

	def front(self):
		assert(len(self.queue))
		return self.queue[0]

	def rear(self):
		assert(len(self.queue))
		return self.queue[-1]

	def isEmpty(self):
		return self.size()==0

q=Queue1()
q.enqueue(9)
print(q.dequeue())
print(q.size())
print(q.isEmpty())
q.enqueue(8)
q.enqueue(7)
print(q.front())
print(q.rear())
