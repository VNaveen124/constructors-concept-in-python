#sample.py
class Sample:
	def __init__(self, a=100, b=200):
		print("-------------------------------------------")
		self.a=a
		self.b=b
		print("Val of a :{}".format(self.a))
		print("Val of b :{}".format(self.b))
		print("-------------------------------------------")
	
	
#main program
print("so1 values")
so1=Sample()   # default constructor
print("so2 values")
so2=Sample(1,2) # Parameterized  constructor
print("so3 values")
so3=Sample(10) # Parameterized  constructor
print("so4 values")
so4=Sample(b=55,a=65) # Parameterized  constructor
print("so5 values")
so5=Sample(b=555) # Parameterized  constructor
