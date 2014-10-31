import QlearningExperiment as QLEXP

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
		averageReturn = QLEXP.getLearnedReturn(epsilon,alpha,10000)
		if averageReturn > bestAverageReturn:
			bestAverageReturn = averageReturn
			bestAlpha = alpha
			bestEpsilon = epsilon

# Print off the best values for recording
print("Return: ", bestAverageReturn)
print("Epsilon: ", bestEpsilon)
print("Alpha: ", bestAlpha)
		