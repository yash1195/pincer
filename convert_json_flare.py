import json

fs = open("profileDump_countryCount")
tmp = fs.read()
data = eval(tmp)

final = {}
final["name"] = "flare"

children = []

for i in data.keys():
	tmp = {}
	tmp["name"] = i
	tmp["size"] = data[i]*1000
	print i,data[i]
	children.append(tmp)

final["children"] = children

fs = open("sample_flare.json","w")
fs.write(json.dumps(final))