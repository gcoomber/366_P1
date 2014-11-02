import QlearningExperiment as QLEXP
import sys

# Set the number of trials over which the average return is calculated
# Default to 100 trials with no argument
numTrials = 100
if len(sys.argv) > 1:
	# Use python QlearningExperiment <X> to run X trials
	numTrials = int(sys.argv[1])

# Initialize the best values low
bestAlpa = 0.0
bestEpsilon = 0.0
bestAverageReturn = -10.0

# Loop over possibilities for alpha
alpha = 0.0
for i in range(9):
	alpha += 0.1
	epsilon = 0.0
	# Loop over possibilities for epsilon
	for j in range(9):
		epsilon += 0.1
		
		# If return is better, update the best values
		averageReturn = QLEXP.getLearnedReturn(epsilon,alpha,numTrials)
		if averageReturn > bestAverageReturn:
			bestAverageReturn = averageReturn
			bestAlpha = alpha
			bestEpsilon = epsilon

# Print off the best values for recording
print("Return: ", bestAverageReturn)
print("Epsilon: ", bestEpsilon)
print("Alpha: ", bestAlpha)
		