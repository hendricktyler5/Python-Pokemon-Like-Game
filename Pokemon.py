"""
Pokemon.py
imports: Character.py

This file contains the main function of this Pokemon style battle game

Written by Tyler Hendrick
"""

from Character import Character
from random import randint

def main():
	#Create opponent and player objects
	you = Character(1)
	computer = Character(2)

	print "Welcome to the Battle Arena!. Here you will be pitted up against a computer opponent and your strategical thinking will be put to the test. A Quick desription of how the game works!\nFirst a coin will be tossed to determine who goes first"
	print "If it is your turn, you will pick a move to make. You can type 4 to see a description of the moves"
	print "Turns will carry out until either you or the computer's health pool reaches 0!\n   Good Luck!"
	
	#Determines who goes first
	x = randint(0,1)
	if(x==0):
		print "You go First!"
	else:
		print "The computer goes First!"
	
	#Loops through turns until either the player quits, or someone loses
	while True:
		if(x == 0):
			print "It is your turn!"
			you.Choice()
			while(you.choice == 4):
				descriptions()
				you.Choice()
			if(you.choice == 5):
				print "You choose to quit!"
				break
			you.battle(computer)
			x = 1
		else:
			print "It is the computer's turn!"
			computer.Choice()
			computer.battle(you)
			x = 0
			
		you.State(computer)
		if (you.defeat != 0):
			print "Game Over\nYou Lost!"
			break
		elif (computer.defeat != 0):
			print "Game Over\nYou Win!"
			break
		
def descriptions():
	print "\nHard Attack is a move that inflicts 17-25 points of damage, but has a miss rate of 40%\nQuick Attack inflicts 7-12 points of damage and has a 10% miss rate\nHeal will restore 5-15 health points but has a miss rate of 20%\n"
	
	
if __name__ == '__main__':	
	main()