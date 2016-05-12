from datetime import datetime
import random, requests, json, time

class Valve(object):
	
	def __init__(self):
		self.position = 0.0
		self.temperature = 0.0
		self.voltage = 0.0
		self.batery_level = 0.0

	def randValues(self):
		self.position = random.randrange(0, 100)
		self.temperature = random.randrange(-10, 300)
		self.voltage = random.randrange(200, 240)
		self.batery_level = random.randrange(0, 100)

	def toJson(self):
		self.randValues()
		return '{"attributes":[{"name":"position","value":"%s"},{"name":"temperature","value":"%s"},{"name":"voltage","value":"%s"},{"name":"batery_level","value":"%s"}]}' % (self.position, self.temperature, self.voltage, self.batery_level)
	


url = "http://127.0.0.1:1026/v1/contextEntities/Valve1"
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

v = Valve()

for i in range(10):
	now = datetime.now()
	r = requests.put(url, data=v.toJson(), headers=headers)
	end = datetime.now()
	print(end - now)
	print(i)
	print(r.json())
	print("\n")
	time.sleep(3)
