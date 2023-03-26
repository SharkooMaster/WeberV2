
from weberParser import parser
from weberToken import token

class compiler:
	def __init__(self):
		print("init compiler")
		self.grammer = [
			["LE"],
			
			["global", "STRING", "EQ", "STRING", "SC"],
			["global", "STRING", "EQ", "STRING", "LE"],
			["global", "STRING", "EQ", "STR", "STRING", "STR", "SC"],
			["global", "STRING", "EQ", "STR", "STRING", "STR", "LE"],
			
			["local", "STRING", "EQ", "STRING", "SC"],
			["local", "STRING", "EQ", "STRING", "LE"],
			["local", "STRING", "EQ", "STR", "STRING", "STR", "SC"],
			["local", "STRING", "EQ", "STR", "STRING", "STR", "LE"]
		]