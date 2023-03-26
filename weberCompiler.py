
from weberParser import parser
from weberToken import token

class exec:
	_type = ""
	_obj = {}
	def __init__(self, _t, _o):
		self._type = _t
		self._obj = _o

class compiler:
	def __init__(self):
		print("init compiler")
		self.grammar = [
			["LE"],
			
			["global", "STRING", "EQ", "STRING", "SC"],
			["global", "STRING", "EQ", "STRING", "LE"],
			["global", "STRING", "EQ", "STR", "STRING", "STR", "SC"],
			["global", "STRING", "EQ", "STR", "STRING", "STR", "LE"],
			
			["local", "STRING", "EQ", "STRING", "SC"],
			["local", "STRING", "EQ", "STRING", "LE"],
			["local", "STRING", "EQ", "STR", "STRING", "STR", "SC"],
			["local", "STRING", "EQ", "STR", "STRING", "STR", "LE"],

			["OPT", "STRING"],
			["SC", "STRING", "EQ", "STR", "STRING", "STR"],
			["SC", "STRING", "EQ", "CBO", "STR", "STRING", "STR", "CBE"],
			["SC", "STRING", "EQ", "CBO", "STRING", "CBE"],
			["CLT"],
			["OPT", "STRING", "CLT"],
		]
		self.execute = ["null", "cgv", "cgv", "cgv", "cgv", "clv", "clv", "clv", "clv", "hto", "hta", "hta", "hta", "hta", "htc", "htc"]
	
	def compile(self, _t):
		execArr = []
		for i in range(len(_t)):
			for j in self.grammar:
				l = len(j)
				_tc = _t[i:i+l]
				
				#Tokens to types / vals
				_tt = []
				_tv = []
				for k in _tc:
					_tt.append(k._type)
					_tv.append(k.value)
				
				#Compare to current rule
				if(_tt == j):
					execArr.append(exec(self.execute[self.grammar.index(j)], _tv))
					break
		for x in execArr:
			if(x._type != "null"):
				print(f"{x._type}::{x._obj}")
