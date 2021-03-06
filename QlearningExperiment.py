import blackjack

from numpy import *
from random import *
from scipy import *
numEpisodes = 1000000

# Learn a policy and calculate the average return from it
def getLearnedReturn(epsilon, alpha, numEpisodes):
	totalReturn = 0.0
	Q = getActionValues(epsilon, alpha, numEpisodes)
	for i in range(numEpisodes):
		G = runLearnedPolicy(Q)
		totalReturn += G
	return totalReturn/numEpisodes

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
	
# Returns the learned policy's action for a given state
def getLearnedPolicy(ActionValues, state):
	assert(state >= 0 and state < 182);
	return argmax(ActionValues[state, :])
	
def runLearnedPolicy(ActionValues):
	G = 0
	# Init the game of blackjack and get the initial state
	s = blackjack.init()
	#Consider each step of the episode
	while s!=-1: #-1 is terminal
		# Take the action given by learned policy
		a = getLearnedPolicy(ActionValues, s)
		r,sp = blackjack.sample(s,a)
		G += r
		s=sp
	return G

def getActionValues(epsilon, alpha, numEpisodes):
	# There are 181 different states (including start state)
	# At each state there are two possible actions 0 or 1, ie stick or hit
	M = 181
	N = 2

	# Create a M x N array filled with zeros, where N is the number of 
	# possible states and M is the number of possible actions at each state
	Q = zeros((M, N))

	returnSum = 0.0
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
			r,sp = blackjack.sample(s,a)
			# Update action value function with Q-learning off-policy update
			Q[s, a] = Q[s, a] + alpha * (r + max(Q[sp, :]) - Q[s, a])
			G += r
			s=sp
	return Q

#print(getLearnedReturn(0.1,0.01,1000))
#blackjack.printPolicy(getLearnedPolicy)

# Run learned policy
#policySum = 0.0
#for policyEpisodeNum in range(numEpisodes):
#	policySum += runLearnedPolicy()

#print("Average learned policy return: ", policySum/numEpisodes)
