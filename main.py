from weberParser import parser
import sys

class page:
	fileName = ""
	fileExt = ""
	fileContent = ""
	
	variables = []
	functions = []
	def __init__(self, _fn, _fe, _fc):
		self.fileName = _fn
		self.fileExt = _fe
		self.fileContent = _fc

x = parser()
t = ""
with open(str(sys.argv[1]), "r", encoding='utf-16') as f: 
	t = f.read()
x.LR(t)

'''
global x = 'hello';
local y = 'bye';

function jsF()
{
	let x = {}
}

<!doctype html>
<html>
	<head>
	</head>
	<body>
	</body>
</html>
'''