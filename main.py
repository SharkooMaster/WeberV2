from weberParser import parser
from weberCompiler import compiler
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
_t = x.LR(t)
c = compiler()
c.compile(_t)

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