"""
Character.py
This file contains the base class of the Pokemon style battle game.

Written by Tyler Hendrick
"""

from random import randint

class Character:
	
	#Constructor
	def __init__(self, player):
		self.health = 100
		self.player = player
		self.defeat = 0
		self.choice = 0
	
	#Carries out adjustments of health of the players
	def battle(self, opponent):
		if(self.choice == 1):
			damage = randint(17, 25)
			opponent.health -= damage
		elif(self.choice == 2):
			damage = randint(7,12)
			opponent.health -= damage
		elif(self.choice == 3):
			healing = randint(5,15)
			if(self.health + healing >= 100):
				print "100 is the max health possible"
				self.health = 100
			else:
				self.health += healing
		elif(self.choice == 0):
			print "Action Missed!"
				
		if(self.health <= 0):
			self.defeat = 1
		elif(opponent.health <= 0):
			opponent.defeat = 1
			
	#Lets players choose their action and controls computer's actions		
	def Choice(self):
		if(self.player == 1):
			self.choice = input("Choose your Action:\n1. Hard Attack\n2. Quick Attack\n3. Heal\n4. Descriptions\n5. Quit\n")
			
		else:
			if(self.health >=30):
				self.choice = randint(1,3)
				if(self.choice == 1):
					print "The computer attempts hard attack"
				elif(self.choice == 2):
					print "The computer attempts quick attack"
				else:
					print "The computer attempts to heal"
					
			elif(self.health <= 10):
				self.choice = 3
			else:
				self.choice = randint(1,5)
				if(self.choice == 4 or self.choice == 5):
					self.choice = 3
				
		success = randint(1,10)
		if(self.choice == 1 and success > 6):
			self.choice = 0
		elif(self.choice == 2 and success > 9):
			self.choice = 0
		elif(self.choice == 3 and success > 8):
			self.choice = 0

	#States players' health after each turn
	def State(self, computer):
		print "\nYour health is %d" %self.health
		print "Your opponent's health is %d\n" %computer.health
		