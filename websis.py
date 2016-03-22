from robobrowser import RoboBrowser

#initialize browser
br = RoboBrowser(history=True)
br.open('http://websismit.manipal.edu/websis/control/main')
form = br.get_form(action="/websis/control/createAnonSession")
form["idValue"].value = "130911017"
form["birthDate"].value = "01-01-1995"
br.submit_form(form)

#returns a dictionary with the details
# def scrapeProfile(regNo,link):
# 	br.open(link)
# 	tmp = {}
# 	tmp['_rollNo']		= regNo
# 	tmp['_name']		= br.select('.full-name')
# 	tmp['_ugCourse']	= br.select('.degree')
	



# #List of all the Registration numbers -> LinkedIn Links
# userLinks = []

# #tsting
# tmpLink = {}
# tmpLink['130911017'] = 'https://www.linkedin.com/in/yash-choukse-31500656?'
# userLinks.append(tmpLink)

# #list of all the scraped users
# userList = []
# tmpProfile = {}


print br.parsed