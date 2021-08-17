import random
class dice(object):#class for each dice
	dice_exist = []

	def __init__(self):
		self.hold = False
		self.value = None
		dice.dice_exist.append(self)
	def roll_dice(self):
		if self.hold != True:
			self.value = random.randint(1,6)
	def change_dice(self, boolean):
		self.hold = boolean


def clear_dice():#clears dice for new roll
	dice.dice_exist = []


def roll():#rolls all dice, returns list of the five dice that are unrolled
	for die in dice.dice_exist:
		dice.roll_dice(die)
	d = []
	for die in dice.dice_exist:
		d.append(die.value)
	return d

def hold(die):#holds a dice
	dice.change_dice(die, True)


def unhold(die):#unholds a dice
	dice.change_dice(die, False)

def make_dice():
	if dice.dice_exist == []:
		for x in range(5):
			dice()
	else:
		return "Dice already exit"

#hands
def numbers(dice_list, number):
	if extra_yahtzee() == 100:
		return 100
	score_value = 0
	for die in dice_list:
		if die.value == number:
			score_value += 1
	return score_value

def ones():
	return numbers(dice.dice_exist, 1)

def twos():
	return numbers(dice.dice_exist, 2)

def threes():
	return numbers(dice.dice_exist, 3)

def fours():
	return numbers(dice.dice_exist, 4)

def fives():
	return numbers(dice.dice_exist, 5)

def sixes():
	return numbers(dice.dice_exist, 6)

def three_of_kind():
	if extra_yahtzee() == 100:
		return 100
	score_value = 0
	if ((ones() >= 3) or (twos() >= 3) or (threes() >= 3) or (fours() >= 3) or (fives() >= 3) or (sixes() >= 3)):
		for die in dice.dice_exist:
			score_value += die.value
	return score_value

def four_of_kind():
	if extra_yahtzee() == 100:
		return 100
	score_value = 0
	if ((ones() == 4) or (twos() == 4) or (threes() == 4) or (fours() == 4) or (fives() == 4) or (sixes() == 4)):
		for die in dice.dice_exist:
			score_value += die.value
	return score_value

def full_house():
	if extra_yahtzee() == 100:
		return 100
	if (((ones() == 3) or (twos() == 3) or (threes() == 3) or (fours() == 3) or (fives() == 3) or (sixes() == 3)) and ((ones() == 2) or (twos() == 2) or (threes() == 2) or (fours() == 2) or (fives() == 2) or (sixes() == 2))):
		return 25
	else:
		return 0

def sm_straight():
	if extra_yahtzee() == 100:
		return 100
	if  ( ( (ones() >= 1) and (twos() >= 1) and (threes() >= 1) and (fours() >= 1) ) or ((twos() >= 1) and (threes() >= 1) and (fours() >= 1) and (fives() >= 1)) or ((threes() >= 1) and (fours() >= 1) and (fives() >= 1) and (sixes() >= 1))):
		return 30
	else:
		return 0

def lrg_straight():
	if extra_yahtzee() == 100:
		return 100
	if (((ones() == 1) and (twos() == 1) and (threes() == 1) and (fours() == 1) and (fives() == 1) and (sixes() == 0)) or ((ones() == 0) and (twos() == 1) and (threes() == 1) and (fours() == 1) and (fives() == 1) and (sixes() == 1))):
		return 40
	else:
		return 0

def yahtzee():
	lst = dice.dice_exist
	if ( (lst[0].value == lst[1].value) and  (lst[1].value == lst[2].value) and (lst[2].value == lst[3].value) and (lst[3].value == lst[4].value) ):
		return 50
	else:
		return 0

def chance():
	if extra_yahtzee() == 100:
		return 100
	score_value = 0
	for die in dice.dice_exist:
		score_value += die.value
	return score_value

def extra_yahtzee():
	if yahtzee() == 50:
		return 100
	else:
		return 0





