import json,http.client,time
ParseData = {
	'Addres':'api.parse.com',
	'port': 443,
	'AppKey':'rwSpEIth88vMWsLr4uTR4YnlyPYW3X0I6UgaWz8b',
	'APIkey':'HBYG6SfkEApOWM3ljZ61k4gMIup6bLsmfHdUMDxS',
	'Class':'Tasks',
	'dataHead':'results'
}
class standard:
	def newLine(num):
		for e in range(0,int(num)):
			print('\n')
	def Menu(StuffDo):
		i = 0
		for e in StuffDo:
			print('{} - {}'.format(i,e))
			i = i + 1
		print(">>>-<<<")
		inputVal = input('int >>')
		if int(inputVal) > len(StuffDo):
			while int(inputVal) > len(StuffDo):
				print('opps try again')
				inputVal = input('int >>')
		return StuffDo[int(inputVal)]
class dataPlay:
	def cheackData(obj,forObj,item):
		for e in obj: #obj must be a list of dicts!
			if e[forObj] == str(item):
				return True
		return False
	def GetJson(): #gets json from parse.
		c = http.client.HTTPSConnection(ParseData['Addres'], ParseData['port'])
		c.connect()
		c.request('GET', '/1/classes/{}/'.format(ParseData['Class']), '', {"X-Parse-Application-Id":ParseData['AppKey'],"X-Parse-REST-API-Key":ParseData['APIkey']})
		Jobject = json.loads(c.getresponse().read().decode())
		temp = []
		for each in Jobject[ParseData['dataHead']]:
			temp.append(each)
		return temp
	def AddData(taskInput):
		c = http.client.HTTPSConnection(ParseData['Addres'], ParseData['port'])
		c.connect()
		c.request('POST', '/1/classes/{}/'.format(ParseData['Class']), json.dumps({'Task':'{}'.format(taskInput)}), { "X-Parse-Application-Id": str(ParseData['AppKey']),"X-Parse-REST-API-Key": str(ParseData['APIkey'])})
		Jobj = json.loads(c.getresponse().read().decode())
		##check if the data has been added
		if dataPlay.cheackData(dataPlay.GetJson(),'Task',str(taskInput)):
			 print('upload Done')
		else:
			print('upload is unsuccessful')
	def delData(taskInput):
		delcheck = False
		for e in dataPlay.GetJson():
			if e['Task'] == str(taskInput):
				temp = e['objectId']
				connection = http.client.HTTPSConnection('api.parse.com', 443)
				connection.connect()
				connection.request('DELETE', '/1/classes/Tasks/{}'.format(temp), '', { "X-Parse-Application-Id": str(ParseData['AppKey']),"X-Parse-REST-API-Key": str(ParseData['APIkey'])})
				delcheck = True
		if delcheck:
			print('Data Deleted')
		else:
			print('Error')
	def AppStart():
		#val = standard.menu(['read','add','del','exit'])
		WhileLoop = True
		while WhileLoop:
			val = standard.Menu(['read','add','del','exit'])
			if val == 'read':
				i = 0
				for e in dataPlay.GetJson():
					print('+ {}'.format(e['Task']))
				input('nul >>')
				standard.newLine(2)
			elif val == 'add':
				standard.newLine(10)
				print('Enter New Data')
				val = input('str >>')
				dataPlay.AddData(val)
			elif val == 'del':
				temp = []
				Json = dataPlay.GetJson()
				i = 0
				for e in json:
					print('{} - {}'.format(i,e['Task']))
					i = i + 1
					temp.append(e['objectId'])
			elif val == 'exit':
				WhileLoop = False
dataPlay.AppStart()
