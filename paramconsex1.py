#paramconsex1.py
class Test:
	def __init__(self, a,b):
		self.a=a
		self.b=b

t1=Test(10,20)
print("Content of t1=", t1.__dict__)
t2=Test(100,200)
print("Content of t2=", t2.__dict__)
t3=Test(1000,2000)
print("Content of t3=", t3.__dict__)
