class token:
	value = None
	_type = None	# ' ' & " " (STRING) : (FLOAT) : (OP)
	def __init__(self, v, t):
		self.value = v
		self._type = t
	
	def __str__(self) -> str:
		return self._type