from weberParser import parser
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
x.LR("global test = 123;\nlocal test2 = 'hello how';\nfunction(arg){print('asd');}")

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