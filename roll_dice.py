# The goal of this script is to check whether two rolls of a dice either sum upto 7 or 11.
import random

min = 1
max = 6
roll_again = "yes"
die1 = random.randint(1,6)
die2 = random.randint(1,6)
print("The dice rolled: {}, {}".format(die1, die2))
print("The sum of dice rolled values is {}".format(die1 + die2))
if (die1 + die2) == 7 or (die1 + die2)== 11:
	print("You win!")
else:
    print("you lost")
