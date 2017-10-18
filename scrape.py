from robobrowser import RoboBrowser
import re
import json
#initialize browser
br = RoboBrowser(history=True,parser="lxml")
br.open('https://www.linkedin.com/')
form = br.get_form(action="https://www.linkedin.com/uas/login-submit")
br.submit_form(form)

#strips all tags
def stripTags(inpText):
	outText = ''
	outText = re.sub(r"^<.*>$","",inpText)
	return outText

#returns a dictionary with the details
def scrapeProfile(regNo,link):
	print "\r> Scraping LinkedIn for Registration No. %s" % regNo
	try:
		br.open(link)
	except:
		pass
	tmp = {}

	tmp['_rollNo']		= regNo
	#Name
	try:
		x 				= br.select('.full-name')[0].text.encode('UTF8')
	except:
		x 				= ""

	tmp['_name']		= x
	#profile link
	tmp['_profileLink']	= link
	
	#get education
	#contains all educations
	tmp['_eduList']		= []

	eduList = br.select('.education')
	for i in range(0,len(eduList)):
		t = {}
		try:
			t['_instituteName'] = stripTags(eduList[i].select('.summary')[0].text.encode('UTF8'))
		except:
			pass
		try:
			z 					= stripTags(eduList[i].select('.education-date')[0].text.encode('UTF8'))
		except:
			pass
		try:
			t['_date']			= z.replace("\xe2\x80\x93","-")
		except:
			pass
		try:
			t['_degree'] 		= stripTags(eduList[i].select('.degree')[0].text.encode('UTF8'))
		except:
			pass
		try:
			t['_major'] 		= stripTags(eduList[i].select('.major')[0].text.encode('UTF8'))
		except:
			pass

		tmp['_eduList'].append(t)

	#remove everything before the word current after stripping tags. ls contains list of companies
	try:
		x =  stripTags(br.select('#overview-summary-current')[0].text.encode('UTF8'))
		x = re.sub(r"^.*Current","",x)
		ls = x.split(",")
		lsn = []
		for i in ls:
			j = {}
			j['company'] = i.strip()
			lsn.append(j)
		tmp['_company'] = lsn
	except:
			pass

	#Getting designation
	try:
		x 				= stripTags(br.select('#headline')[0].text.encode('UTF8'))
	except:
		x 				= ""

	tmp['_designation'] = x

	#Getting industry
	try:
		x 				= stripTags(br.select('.industry')[0].text.encode('UTF8'))
	except:
		x 				= ""

	tmp['_industry'] = x

	#Getting location
	try:
		x 				= stripTags(br.select('.locality')[0].text.encode('UTF8'))
	except:
		x 				= ""

	tmp['_location'] = x
	
	userList.append(tmp)
	



#List of all the Registration numbers -> LinkedIn Links
userLinks = []

#tsting
tmpLink = {}
tmpLink['130911020'] = 'https://www.linkedin.com/in/mehulsmritiraje'
tmpLink['130912222'] = 'https://www.linkedin.com/in/mehulsmritiraje'
userLinks.append(tmpLink)

#list of all the scraped users
userList = []

#reading input from file
with open("in.csv", "rw+") as fs:
	linkList = fs.read().splitlines()

for i in linkList:
	k,v = i.split(',')
	if v == "":
		tmp = {}
		tmp['_rollNo']		= k
		userList.append(tmp)
	else:
		scrapeProfile(k,v)



with open("list.json","w") as f:
    json.dump(userList,f)



