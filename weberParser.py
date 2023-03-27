from weberToken import token

class parser:
	def __init__(self):
		print("Parsing")
		self.ops = ["{","}","[","]","(",")","=",";","'",'"',"\n","<",">", "<?", "?>", "?", "\t"]
		self.opsN= ["CBO","CBE","BO","BE","BRO","BRE","EQ","SC", "STR", "STR","LE","OPT","CLT", "COT", "COE", "QU", "LT"]
		self.synt= ["global", "local"]

	def LR(self, s):
		_s = s
		a = 0
		tokens = []
		stack=[]
		skipStep = False
		for ind,i in enumerate(s):
			if(skipStep):
				if(len(stack)!=0):
					tokens.append(token(combStack, "STRING"))
					stack.clear()
				a += ind
				_s = s[ind:]
				skipStep = False
			else:
				_i = i
				combStack = "".join(stack)
				#combStack = combStack.replace(" ", "")
				if(i in self.ops):
					if(len(stack)!=0):
						tokens.append(token(combStack, "STRING"))
						stack.clear()
					
					if(ind < len(s)-1 and not skipStep):
						if(i+s[ind+1] in self.ops):
							print(i+s[ind+1])
							tokens.append(token(i+s[ind+1], self.opsN[self.ops.index(i+s[ind+1])]))
							skipStep = True
						else:
							tokens.append(token(i, self.opsN[self.ops.index(i)]))
					else:
						tokens.append(token(i, self.opsN[self.ops.index(i)]))
					_i = ""

				if(combStack in self.synt):
					stack.clear()
					tokens.append(token(combStack, combStack))
				a += 1
				_s = s[a:]
				stack.append(_i)

		if(len(stack)!=0):
			tokens.append(token(combStack, "STRING"))
			stack.clear()
		ret = []
		for j in tokens:
			if(j.value != "" and j.value != " "):
				ret.append(j)
				print(f"TOKEN:: {j._type} -> {j.value}")
		return ret
