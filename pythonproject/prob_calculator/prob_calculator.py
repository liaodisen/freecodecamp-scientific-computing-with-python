import copy
import random
# Consider using the modules imported above.

class Hat:
	contents = []
	dict0 = {}
	
	def __init__(self, **balls):
		self.dict0 = balls
		for ball, times in balls.items():
			for i in range(0, times):
				self.contents.append(ball)

	def draw(self, number):
		result = []
		if number >= len(self.contents):
			result = self.contents
			self.contents = []
			return result
		else:
			for i in range(0, number):
				pull = random.randint(0, len(self.contents)-1)
				result.append(self.contents[pull])
				del self.contents[pull]
			return result
	
def draw_from_dic(dic, number):
	contents = []
	result = []
	for ball, times in dic.items():
		for i in range(0, times):
			contents.append(ball)
	if number >= len(contents):
		result = contents
		return result
	else:
		for i in range(0, number):
			pull = random.randint(0, len(contents)-1)
			result.append(contents[pull])
			del contents[pull]
		return result
		

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	dict2 = dict()
	dict1 = hat.dict0.copy()
	n = 0
	for times in range(0,num_experiments):
		dict2 = dict()
		draw_result = draw_from_dic(dict1, num_balls_drawn)
		for thing in draw_result:
			if thing not in dict2:
				dict2[thing] = 1
			else:
				dict2[thing] = dict2[thing] + 1
		if dict2 == expected_balls:
			n = n + 1
	return n/num_experiments
	
