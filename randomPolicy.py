import blackjack

from numpy import *
from random import *
from scipy import *
numEpisodes = 20


def showOneGame():
	s=blackjack.init()
	moves=[0,1,0] 
	turn=0
	while s!=-1: #-1 is terminal
		a=moves[turn]
		r,sp=blackjack.sample(s,a)
		print("turn %d: s %d a %d -> r %d sp %d "%(turn,s,a,r,sp),end="")
		print("\t Player Sum: %d  Dealer Card: %d  Usable Ace: %d"%(blackjack.playerSum,blackjack.dealerCard, blackjack.usableAce))
		s=sp
		turn+=1
	return None


returnSum = 0.0
for episodeNum in range(numEpisodes):
	# Cumulative reward
	G = 0
	# Create a new seed for the random number generator
	random.seed(episodeNum)
	# Init the game of blackjack and get the initial state
	s = blackjack.init()
	# Generate a random action (0 for stick or 1 for hit) at the current state
	# for each step of the episode. Take random action and observe the reward.
	while s!=-1: #-1 is terminal
		a = random.randint(0,2)
		r,sp = blackjack.sample(s,a)
		G += r
		s=sp
	print("Episode: ", episodeNum, "Return: ", G)
	returnSum = returnSum + G
print("Average return: ", returnSum/numEpisodes)

