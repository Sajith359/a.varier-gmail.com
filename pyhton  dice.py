Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> min=1
>>> max=6
>>> roll_again="yes"
>>> die1 = random.randint(1,6)
>>> die2 = random.randint(1,6)
>>> print(die1, die2)
6 5
>>> print(die1 + die2)
11
>>> if (die1 + die2) == 7 or (die1 + die2)== 11:
	print("You win!")

else:

  print("you lost")
  