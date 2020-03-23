import itertools
import random
import time

"""Creates new Deck of 6 decks """
def newDeck():
	deck = []
	for i in range(24):
		deck.append(list(range(1,13)))
	deck = sum(deck, [])	
	return deck

"""Calculates player hand returns score"""
def calculateHand(hand):
	handValue = hand.copy()
	handSize = len(handValue)
	for i in range(handSize):
		if handValue[i] == 11 or handValue[i] == 12 or handValue[i] == 13:
			handValue[i] = 10

	"""Checks if theres an ACE and checks whether it can be 11 points if not keep it 1"""
	for i in range(handSize):
		if handValue[i] == 1:
			handValue[i] = 11
			if sum(handValue) > 21:
				handValue[i] = 1

	return sum(handValue)

"""Prints player status and dealers hand without showing all dealers cards"""
def printStatus(playerHand, computerHand):
	print("Starting Game!")
	print("Your Hand")
	print(playerHand)
	print("Your Score")
	print(calculateHand(playerHand))
	print("")
	print("Dealers Hand")
	print(f"[{computerHand[1]}, X]")
	print("")


"""Players turn ask for user input"""
def playerTurn(hand):
	print("Your Turn!")
	while calculateHand(hand) < 21:
		print("")
		print("1:Hit me, 2:Hold")
		playerInput = input()
		if playerInput == "1":
			hand += deck[:1]
			deck.remove(deck[0])
			print(hand)
			print(calculateHand(hand))
		if playerInput == "2":
			break

"""Plays computers turn where we dont hit if equal to or greater than 17"""
def computerTurn(hand):
	while calculateHand(hand) < 17:
		print("")
		print("Dealer Hit's")
		hand += deck[:1]
		deck.remove(deck[0])
		print("Dealers Hand")
		print(hand)
		print("Dealers Score")
		print(calculateHand(hand))		
		time.sleep(3)

def printScore(playerHand, computerHand):
	print("")
	print("Your Hand")
	print(playerHand)
	print("Your Score")
	print(calculateHand(playerHand))
	print("")
	print("Dealers Hand")
	print(computerHand)
	print("Dealers Score")
	print(calculateHand(computerHand))

def playGame(deck):
	"""Create player hand remove two cards from deck"""
	playerHand = deck[:2]
	deck = deck[2:-2]

	computerHand = deck[:2]
	deck = deck[2:-2]

	printStatus(playerHand,computerHand)

	"""Check if dealer has blackjack"""
	if calculateHand(computerHand)  == 21:
		print("Dealer Blackjack you lose")
		return
	elif calculateHand(playerHand) == 21:
		print("Blackjack you win")
		return

	playerTurn(playerHand)
	if calculateHand(playerHand) > 21:
		print("Bust you lose")
		return
	computerTurn(computerHand)
	if calculateHand(computerHand) > 21:
		print("Dealer Bust you win")
		return


	printScore(playerHand,computerHand)
	if calculateHand(playerHand) > calculateHand(computerHand):
		print("Player wins")
	elif calculateHand(playerHand) < calculateHand(computerHand):
		print("Dealer wins")
	else:
		print("Push")
	return


deck = newDeck()
random.shuffle(deck)
gameRunning = True
playGame(deck)
while gameRunning:
	"""Create new deck if under half the size of 6 decks"""
	if len(deck) < 156:
		deck = newDeck()
		random.shuffle(deck)
	print("")
	print("Play again 1:Yes, 2:No")
	playerInput = input()
	if playerInput == "1":
		random.shuffle(deck)
		playGame(deck)
	elif playerInput == "2":
		gameRunning = False