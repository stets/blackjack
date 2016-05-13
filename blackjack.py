#/usr/bin/python
# encoding=utf8

import random

cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
playerHand = []
#playerHand = [1,2,3,4,5,6,7,8,9,10,'J','Q','K', 'A']

print "Welcome to the Casino!"
print "Get ready to bet!"

def main():
	hitorstay = raw_input("\n[H] to Hit or [S] to Stay:")
	if hitorstay == "H" or hitorstay == "h":
		print "you're hitting!"
		hit()
	elif hitorstay == "S" or hitorstay == 's':
		print "you're staying!"


def hit():
	#pick a random that is the size of the deck
	print 'echo debug'	
	randNum = random.randint(0,len(cards)-1)
#	cardPull = cards[randNum]

	#add the card to players hand
#	playerHand.append(cardPull)
	playerHand.append(cards[randNum])
	#delete from deck	
	del cards[randNum]
	myScore()

def myScore():
	score = []
	y = 0
	for x in playerHand:
		y+=1
		if x == 'J' or x == 'Q' or x == 'K':
			score.append(10)
		elif x == 'A':
			score.append(11)
		else:
			score.append(playerHand[y-1])
	print "Hand:", playerHand, 'worth:', sum(score)
	if sum(score) == 21:
		print "You win!"
	elif sum(score) < 21:
		print "You haven't bust yet, hit again?"
		gambleon = raw_input ("[h] to hit ")
		if gambleon == 'h':
			hit()
		else:
			pass
	elif sum(score) > 21:
		print "you lose"

main()

