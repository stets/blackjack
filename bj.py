#!/usr/bin/env python
import random

playerHand = []
dealerHand = []
playerScore = 0


cards = ['AH', 'JH', 'QH', 'KH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'AC', 'JC', 'QC', 'KC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'AD', 'JD', 'QD', 'KD', '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'AS', 'JS', 'QS', 'KS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S']


print "\n\nThere are " + str(len(cards) - 1) + " cards in the deck before the deal\n"

def dealplayer():
	x = random.randrange(0,len(cards)-1)

	playerHand.append(cards[x])
	cards.remove(cards[x])


	print "The player has", playerHand
#	print cards
#	print "\n\nThere are " + str(len(cards) - 1) + " cards in the deck after the deal\n\n"


def dealdealer():
	x = random.randrange(0,len(cards)-1)

	dealerHand.append(cards[x])
	cards.remove(cards[x])


#	print "The dealer has" , dealerHand
#	print cards
#	print "\n\nThere are " + str(len(cards) - 1) + " cards in the deck after the deal\n\n"

def hitagain():
	playerScore = 0
	x = random.randrange(0,len(cards)-1)

	playerHand.append(cards[x])
	cards.remove(cards[x])
	plCard3 = playerHand[2]	

	print "The player has", playerHand
	
	if plCard3[0] == 'J' or plCard2[0] == 'Q' or plCard2[0] == 'K' or plCard2[:2] == '10':
		playerScore = playerScore + 10

	elif plCard3[0] == 'A':
		playerScore = playerScore + 11

	elif plCard3[0] == plCard3[0]:
		playerScore =  playerScore + int(plCard3[0])
	if playerScore == 21:
		print "You got blackjack!"

	print "Score is:", playerScore
dealplayer()
dealplayer()

plCard1 = playerHand[0]
plCard2 = playerHand[1]

if plCard1[0] == 'J' or plCard1[0] == 'Q' or plCard1[0] == 'K' or plCard1[:2] == '10':
	playerScore = 10

elif plCard1[0] == 'A':
	playerScore = 11

elif plCard1[0] == plCard1[0]:
	playerScore = int(plCard1[0])

#start check of second card
if plCard2[0] == 'J' or plCard2[0] == 'Q' or plCard2[0] == 'K' or plCard2[:2] == '10':
	playerScore = playerScore + 10

elif plCard2[0] == 'A':
	playerScore = playerScore + 11

elif plCard2[0] == plCard2[0]:
	playerScore =  playerScore + int(plCard2[0])
#offer player to hit
if playerScore == 21:
	print "You got blackjack!"

elif playerScore < 21:
	print "Your score is", playerScore, " would you like to hit?"
	hitorstay = raw_input("\ny to hit, n to stand: ")
	if hitorstay == 'y' or hitorstay == 'Y':
		print "u hittin"
		hitagain()
	elif hitorstay == 'n' or hitorstay == 'N':
		print "u stayin doe"
	

