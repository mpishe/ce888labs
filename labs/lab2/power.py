import numpy as np
from random import choices

def permutation_test(data1, data2, size, reps):

	cap = size
	datastack = np.hstack((data1, data2))
	datasize = len(data1)
	
	permutations = []
	for _ in range(reps):
		perm_data = np.random.permutation(datastack)
		permutedata1 = perm_data[:datasize]
		permutedata2 = perm_data[-datasize:]
		permutval = np.mean(permutedata2) - np.mean(permutedata1)
		permutations.append(permutval > cap)

	return np.mean(permutations)

def power(sample1, sample2, reps, size, alpha):

	permutevalues = []
	for _ in range(reps):
		data1 = choices(sample1, k=len(sample1))
		data2 = choices(sample2, k=len(sample2))
		permutevalues = permutation_test(data1, data2, size, 19000)
		pvalues.append(pval)
	
	return np.mean(np.array(permutevalues) < (1.0-alpha))

if __name__ == "__main__":

	olddata = np.array([0,0,0,0,0,0,1,0,0,1,0])
	newdata = np.array([1,0,0,1,1,1,0,0,0,1,0])

	alpha = 0.95
	p = power(olddata, newdata, 10, 11, alpha)
	print(f"Power = {p}")
