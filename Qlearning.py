import blackjack

from numpy import *
from random import *
from scipy import *
numEpisodes = 10000

# Calculate the epsilon greedy action at a given state
def getEpsilonGreedyAction(Q, state, epsilon):
	# epsilon must be between 0.0 and 1.0
	assert (epsilon >= 0.0) and (epsilon <= 1.0)
	# Choose greedy action with probability 1 - epsilon
	action = getGreedyAction(Q, state)
	# Choose random action with probability epsilon
	sample = random.random_sample()
	if sample <= epsilon:
		action = random.randint(0,2)
	return action
	
# Calculate and return the greedy action at the given state
def getGreedyAction(Q, state):
	# Find action at current state, that has the max action value
	greedyAction = argmax(Q[state, :])
	# If both actions have the same action value, choose action at random
	if Q[state, 0] == Q[state, 1]:
		greedyAction = random.randint(0,2)
	return greedyAction

# There are 182 different states (including start and terminal states)
# At each state there are two possible actions 0 or 1, ie stick or hit
N = 182
M = 2

actionStick = 0
actionHit = 1

# Create a N x M array filled with zeros, where N is the number of 
# possible states and M is the number of possible actions at each state
Q = zeros((N, M))

returnSum = 0.0
epsilon = 0.01
alpha = 0.001
for episodeNum in range(numEpisodes):
	random.seed(episodeNum)
	# Cumulative reward
	G = 0
	# Init the game of blackjack and get the initial state
	s = blackjack.init()
	#Consider each step of the episode
	while s!=-1: #-1 is terminal
		# Take epsilon greedy action at each step of episode
		a = getEpsilonGreedyAction(Q, s, epsilon)
		#a = getGreedyAction(Q, s)
		r,sp = blackjack.sample(s,a)
		# Update action value function with Q-learning off-policy update
		Q[s, a] = Q[s, a] + alpha * (r + max(Q[sp, :]) - Q[s, a])
		G += r
		s=sp
	
	print("Episode: ", episodeNum, "Return: ", G)
	returnSum = returnSum + G
	
print("Average return: ", returnSum/numEpisodes)