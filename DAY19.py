def PerfectSquare(start,end):
	for i in range(start,end+1):
		if(i**(.5))==int(i**(.5)):
			print(i,end=" ")

start=1
end=100
PerfectSquare(start,end)