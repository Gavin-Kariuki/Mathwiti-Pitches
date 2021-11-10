class Students:
	def __init__(self, name, reg):
		self.name = name
		self.reg = reg

	def __repr__(self):
		string= f"Student:{self.name}\nReg:{self.reg}"
		return string


