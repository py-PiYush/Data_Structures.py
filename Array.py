class Array:
	def __init__(self):
		self.arr=[]
		self.len=0
		self.cap=0

	def size(self):
		return self.len

	def isEmpty(self):
		if self.len==0:
			return True
		return False

	def index(self,a):
		for i in range(self.len):
			if self.arr[i]==a:
				return i
		return -1

	def remove(self,a):
		for i in range(self.len):
			if self.arr[i]==a:
				pivot=i
				break
		for i in range(pivot,self.len-1):
			self.arr[i]=self.arr[i+1]
		self.len-=1

	def append(self,a):
		if self.len+1>=self.cap:
			if self.cap==0:
				self.cap=1
			else:
				self.cap*=2
			self.new_arr=[-1]*self.cap
			for i in range(self.len):
				self.new_arr[i]=self.arr[i]
			self.arr=self.new_arr
		self.arr[self.len]=a
		self.len+=1

	def print(self):
		for i in range(self.len):
			print(self.arr[i],end=' ')
		print('\n')

arr=Array()
print(arr.size())
arr.append(9)
arr.append(0)
arr.append(7)
arr.print()
print(arr.index(7))
arr.remove(9)
arr.print()



