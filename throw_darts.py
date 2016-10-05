from random import uniform
from numpy import logspace, array
from math import sqrt
from time import time
from os import system

def throw(N_darts,verbose=False):
	from random import uniform
	from math import sqrt
	from time import time

	# Initialize
	N_darts = int(N_darts)
	hit = 0

	start = time()

	# Loop
	for n in range(N_darts):
		x,y = uniform(0,1), uniform(0,1)
		if sqrt((x-0.5)**2 + (y-0.5)**2) <= 0.5:
			hit += 1

	end = time()
	ellapsed = end-start
	rate = float(N_darts) / ellapsed

	pi_approx = 4 * float(hit) / N_darts

	if verbose == True:
		print("Pi Approx:", pi_approx)
		print("N_darts:", N_darts)
		print("Execution Time (s):",ellapsed)
		print("Darts Thrown / Sec:", rate)
	return ellapsed, rate

