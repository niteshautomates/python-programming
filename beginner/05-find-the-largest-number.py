

class FindTheLargestNumber:
	def __init__(self, a, b, c):
		self.a=a
		self.b=b
		self.c=c
  
  
	def find_the_largest_of_three_numbers(self):
		if self.a >= self.b and self.a >= self.c:
			print(f"{self.a} is largest", self.a)
		elif self.b>= self.c and self.b >= self.a:
			print(f"{self.b} is largest", self.b)
		else:
			print(f"{self.c} is largest", self.c)

obj = FindTheLargestNumber(10, 20, 30)
obj.find_the_largest_of_three_numbers()
