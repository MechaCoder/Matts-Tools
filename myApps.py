#V0.2
import json
import http.client
ParseData = {
	'Addres':'api.parse.com',
	'port': 443,
	'AppKey':'[PlaceHold]',
	'APIkey':'[PlaceHold]',
	'Class':'[PlaceHold]',
	'dataHead':'results'
}

class standard:
	''' Tools that may be used in all classes'''
	def newLine(num=1):
		'''. this is witll create a automatic newLine based on a interger placed in an argurement .'''
		for e in range(0,int(num)):
			print('\n')

	def Menu(StuffDo):
		'''. this will make a menu with input and will return the item as a string  Arg is a list.
		'''
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


class TaskList:
	''' taskList Class
		this requires ParseData{} to runs
	 '''
	def cheackData(forObj,item):
		'''. this checks if the the data is in the Database
		the first is arg defines argument, 
		the secound argument is the argument define the row head 
		the third is the value of the item your looking
		.'''
		for e in GetJson():
			if e[forObj] == str(item):
				return True
		return False

	def GetJson(): 
		'''. gets json from parse .'''
		c = http.client.HTTPSConnection(ParseData['Addres'], ParseData['port'])
		c.connect()
		c.request('GET', '/1/classes/{}/'.format(ParseData['Class']), '', {"X-Parse-Application-Id":ParseData['AppKey'],"X-Parse-REST-API-Key":ParseData['APIkey']})
		Jobject = json.loads(c.getresponse().read().decode())
		temp = []
		for each in Jobject[ParseData['dataHead']]:
			temp.append(each)
		return temp

	def AddData(taskInput=''):
		'''. This will imput neew data into the database .'''
		c = http.client.HTTPSConnection(ParseData['Addres'], ParseData['port'])
		c.connect()
		c.request('POST', '/1/classes/{}/'.format(ParseData['Class']), json.dumps({'Task':'{}'.format(taskInput)}), { "X-Parse-Application-Id": str(ParseData['AppKey']),"X-Parse-REST-API-Key": str(ParseData['APIkey'])})
		Jobj = json.loads(c.getresponse().read().decode())
		##check if the data has been added
		if TaskList.cheackData(TaskList.GetJson(),'Task',str(taskInput)):
			 print('upload Done')
		else:
			print('upload is unsuccessful')

	def delData(taskInput):
		'''. deleting data, form the database.'''
		delcheck = False
		for e in TaskList.GetJson():
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
		'''. This will start the App ^_^ .'''
		WhileLoop = True
		while WhileLoop:
			val = standard.Menu(['read','add','del','exit'])
			if val == 'read':
				i = 0
				for e in TaskList.GetJson():
					print('+ {}'.format(e['Task']))
				input('nul >>')
				standard.newLine(2)
			elif val == 'add':
				standard.newLine(10)
				print('Enter New Data')
				val = input('str >>')
				TaskList.AddData(val)
			elif val == 'del':
				temp = []
				Json = TaskList.GetJson()
				i = 0
				for e in json:
					print('{} - {}'.format(i,e['Task']))
					i = i + 1
					temp.append(e['objectId'])
			elif val == 'exit':
				WhileLoop = False

	def SetKeys():
		''' this is too set up the Parse Keys '''
		if ParseData['AppKey'] and ParseData['APIkey'] and ParseData['Class'] == '[PlaceHold]':
			print('Would you like set your key')
			YesNo = input('Y/N >>')
			if YesNo == 'Y' or 'y' or 'yes' or 'Yes' or 'YES':
				print('you need go and find the keys in your app which is held on Parse you are going to need the class, the api key and the app key')
				api_key = input('API key >>')
				app_key = input('App key >>')
				api_cla = input('class   >>')
				print('thank you we just need check the connection')
			elif YesNo == 'N' or 'n' or 'no' or 'No' or 'NO':
				exit()
	
	def NetTest(ip='127.0.0.1', p=80):
	    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    try:
	        con.connect((host, p))
	        con.shutdown(2)
	        return True
	    except socket.error as e:
	        return False
TaskList.AppStart()
