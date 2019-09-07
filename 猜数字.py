"""
plays a game of guess the number with the user.
"""

import random

smaller=int(input("enter the smaller number:"))
larger=int(input("enter the larger number:"))
mynumber=random.randint(smaller,larger)
count=0
while True:
	count+=1
	usernumber=int(input("enter your guess:"))
	if usernumber<mynumber:
		print("too small")
	elif usernumber>mynumber:
		print("too large")
	else:
		print("you've got it in",count,"tries!")
		break