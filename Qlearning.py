import blackjack

from numpy import *
from random import *
from scipy import *
numEpisodes = 20

# There are 182 different states (including start and terminal states)
# At each state there are two possible actions 0 or 1, ie stick or hit

# Create a n x m array filled with zeros, where n is the number of 
# possible states and m is the number of possible actions at each state
np.zeros((182, 2))

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