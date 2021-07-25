class Category:
	funds = 0
	name = ""
	ledger = []
	
	def  __init__(self, x):
		self.name = x
		self.ledger = []
		
	def check_funds(self, amount):
		if self.funds > amount:
			return False
		else:
			return True
	
	def deposit(self, amount, description = ""):
		self.funds += amount
		self.ledger.append({"amount": '%.2f'%amount, "description": description})
	
	def withdraw(self, amount, description = ""):
		if self.funds - amount < 0:
			return False
		else:
			self.funds = self.funds - amount
			self.ledger.append({"amount":('%.2f'%(-1*amount)), "description": description})
			return True
	
	def get_balance(self):
		return self.funds
	
	def transfer(self, amount, another):
		if self.funds - amount < 0:
			return False
		else:
			self.withdraw(amount, "Transfer to"+ " " + another.name)
			another.deposit(amount, "Transfer from"+ " " + self.name)
			return True
	
	def __str__(self):
		num_lines = len(self.ledger)+2
		stars = (30 - len(self.name))//2
		first_line = stars*"*"+self.name+(30-stars-len(self.name))*"*"
		last_line = "Total: " + str(self.get_balance())
		middle = ""
		for event in self.ledger:
			des = event["description"]
			monety = str(event["amount"])
			space = 23 - len(des)
			space2 = 7 - len(monety)
			if space <= 0:
				middle = middle + des[:23] + space2*" " + monety +"\n"
			elif space > 0:
				middle = middle + des + (space+space2)*" " + monety + "\n"
		return first_line + "\n" + middle + last_line
		

def create_spend_chart(categories):
	title = "Percentage spent by category"
	l_list = []
	p_list = []
	alls = 0
	for things in categories:
		l_list.append(things.name)
		alls += things.get_balance()
	for things in categories:
		perc = 100*things.get_balance()/alls
		percent = round(perc, -1)
		p_list.append(percent)
	lines = len(max(l_list, key = len))
	bottom = ""
	main = ""
	for i in range(0, lines):
		bottom = bottom + 5*" "
		for stuff in l_list:
			if i < len(stuff):
				bottom = bottom + stuff[i] + 2*" "
			else:
				bottom = bottom + 3 * " "
		bottom = bottom + "\n"
	for i in range(100, -10, -10):
		if i == 100:
			main = main + "100| "
			for p in p_list:
				if p >= i:
					main = main + "o  "
				else:
					main = main + "    "
		elif i == 0:
			main = main + "  0| "
			for p in p_list:
				if p >= i:
					main = main + "o  "
				else:
					main = main + "    "
		else:
			main = main + " " + str(i) + "| "
			for p in p_list:
				if p >= i:
					main = main + "o  "
				else:
					main = main + "   "
		main = main + "\n"	
	main = main + 4*" " + (1+3*lines)*"-" + "\n" 
	return main + bottom
			

				
		


	
		