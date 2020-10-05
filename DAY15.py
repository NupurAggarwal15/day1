text=open("Nupur.txt","r")
d=dict()
for line in text:
	line=line.strip()
	line=line.lower()
	words=line.split(" ")

	for the in words:
		if the in d:
			d[the]=d[the]+1
		else:
			d[the]=1
for key in list(d.keys()):
	print(key,":",d[key])