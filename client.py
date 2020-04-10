class Client:
	def __init__(self,name):
		self._name=name
		
	def getName(self): 
		return self._name
	def setName(self,val):
		self._name=val
	
	def test(self):
		print "hello world!"