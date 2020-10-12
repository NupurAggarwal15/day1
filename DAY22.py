import random

lower=0
upper=50

x=random.randint(lower,upper)
print("\n\tYou've only 5 chances to guess !\n")

count=0

while count<5:
	count+=1
	guess=int(input("Guess a number: "))

	if x==guess:
		print("Congratulation you did it in",count,"try")
		break
	else: 
		print("Number of chances",5-count,"left")
	

if count>=5:
	print("Better Luck Next Time!")