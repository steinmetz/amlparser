import xml.etree.ElementTree as ETree

class ModelParser(object):
	
	def __init__(self, filename):
		super(ModelParser, self).__init__()
		self.index = 0
		self.filename = filename	
		self.attributes = []	

	def processFile(self):
		e = ETree.parse(self.filename).getroot()
		ih = e.find('InstanceHierarchy')
		ie = ih.find('InternalElement')
		self.findAttributes(ie)
		self.selectAttributes()

	def selectAttributes(self):
		self.showAttributes()
		try:
		    s = raw_input("Input the numbers (e.g. 1 2 3):")
		    numbers = map(int, s.split())

		    self.sendToMiddleware(numbers)

		except ValueError:
		    print "Not a number"

	def sendToMiddleware(self, indexes):
		print("Sending to FIWARE...")
		for x in indexes:
			attr = self.attributes[x]
			print( "[%i] - %s:%s" % (x, attr.get('Name'), self.formatDataType(attr.get('AttributeDataType'))))

	def showAttributes(self): 
		for index, attr in enumerate(self.attributes):
			print( "[%i] - %s:%s" % (index, attr.get('Name'), self.formatDataType(attr.get('AttributeDataType'))))

	def findAttributes(self, ie):
		
		attr = ie.findall('Attribute')

		if len(attr) > 0:
			for x in attr:
				self.attributes.append(x)
				#print(x.get('Name'), self.formatDataType(x.get('AttributeDataType')))
		
		ies = ie.findall('InternalElement')
		for x in ies:
			self.findAttributes(x)

	def formatDataType(self, datatype):
		return datatype[3:]

parser = ModelParser("atuador.aml")
parser.processFile()