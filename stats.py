import os
import re 
from robobrowser import RoboBrowser
import copy

# allFiles = os.listdir("./done")
# jsonDump = []

# chosing .json files

# for i in allFiles:
# 	if i.endswith(".json"):
# 		jsonDump.append(i)

# file1 = jsonDump[2]

# fs = open("./done/"+file1,"r")
fs = open("./done/2005-2009.json","r")

data = eval(fs.read())

# init browser
br = RoboBrowser(history=True,parser="lxml")


# random function

#strips all tags
TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

#second copy of array of users
withCountryProfiles = []

nm = 1

countryCount = {}
mastersUniversities = {}
mastersCount = 0 

for i in data:
	country = "NA"
	try:
		url = "http://api.geonames.org/search?username=zeko&fuzzy=0.7&type=json&name="
		tmp1 = i['_location'].split(",")
		tmp2 = tmp1[0].rsplit(" ",1)
		

		# url not empty
		if tmp2[0]:
			url += tmp2[0]

			#make request for country
			br.open(url)
			tmpData = br.parsed

			# t has text of resp json
			t = remove_tags(repr(tmpData))
			
			resp = eval(t)
			# print type(resp['totalResultsCount'])
			
			if resp['totalResultsCount'] == 0:
				country = "NA"
			else:
				country = resp['geonames'][0]['countryName']
			
	except:
		country = "NA"
	print url
	print country
	#copy of i
	j = copy.deepcopy(i)
	#add country
	j['_countryOfResidence'] = country

	# increase country count
	if country in countryCount.keys():
		countryCount[country] += 1
	else:
		countryCount[country] = 1

	try:
		#increase masters count
		for x in i['_eduList']:
			degree = x['_degree']
			if re.search('master',degree,re.IGNORECASE):
				# increase count
				mastersCount += 1
				uname = x['_instituteName'].title()
				if uname in mastersUniversities.keys():
					mastersUniversities[uname] += 1
				else:
					mastersUniversities[uname] = 1

	except:
		pass

	#add to final list
	withCountryProfiles.append(j)
	# print j
	# print ''
	# # nm += 1
	# # if nm == 15:
	# # 	break

fs = open("profileDump_country","w")
fs.write(str(withCountryProfiles))

fs = open("profileDump_countryCount","w")
fs.write(str(countryCount))

fs = open("profileDump_mastersCount","w")
fs.write(str(mastersCount))

fs = open("profileDump_mastersUniiversities","w")
fs.write(str(mastersUniversities))

