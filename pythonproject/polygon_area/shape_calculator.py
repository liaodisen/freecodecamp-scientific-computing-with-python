class Rectangle:
	cur_width = 0
	cur_height = 0
	
	def __init__(self, width, height):
		self.cur_width = width
		self.cur_height = height
	
	def set_width(self, number):
		self.cur_width = number
	
	def set_height(self, number):
		self.cur_height = number
	
	def get_area(self):
		return self.cur_width * self.cur_height
	
	def get_perimeter(self):
		return 2*(self.cur_width + self.cur_height)
	
	def get_diagonal(self):
		return (self.cur_width ** 2 + self.cur_height ** 2) ** .5
		
	def get_picture(self):
		if self.cur_width > 50 or self.cur_height > 50:
			return "Too big for picture."
		else:
			result = ""
			for i in range(0, self.cur_height):
				for j in range(0, self.cur_width):
					result = result + "*"
				result = result + "\n"
			return result

	def get_amount_inside(self, shape):
		area = shape.get_area()
		res = self.get_area()/area
		return int(res)
		
	def __str__(self):
		return "Rectangle(width=" + str(self.cur_width) + ", height=" + str(self.cur_height) + ")"



class Square(Rectangle):
	side = 0
	
	def __init__(self, side):
		self.side = side
		self.cur_width = side
		self.cur_height = side
	
	def set_side(self, number):
		self.cur_width = number
		self.cur_height = number
		self.side = number
	
	def set_width(self, number):
		self.set_side(number)
		
	def set_height(self, number):
		self.set_height(number)
		
	def __str__(self):
			return "Square(side=" + str(self.side) + ")"
	

	
	
