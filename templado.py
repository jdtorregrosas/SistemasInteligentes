'''def anneal(values, max_iter):
	if len(values) != 0:
		initial_ind = 0
		cal = values[initial_ind]
		best_ind = initial_ind
		best_cal = cal
		k = 0

		while k < max_iter and cal > 0:
			pass

def get_neighbours(values, index, rang):
	neighbours = []
	print values[index-rang:index]
	neighbours.append[values[index-rang:index]]
	neighbours.append[values[index+1:index+1+rang]]
	return neighbours

test = [0,1,2,3,4,5]
print get_neighbours(test, 2, 2)
'''
import random
import math
LIMIT = 100000

def update_temperature(T, k):
    return T - 0.001

def get_neighbors(i, L):
    assert L > 1 and i >= 0 and i < L
    if i == 0:
        return [1]
    elif i == L - 1:
        return [L - 2]
    else:
        return [i - 1, i + 1]

def make_move(x, A, T):
    # nhbs = get_neighbors(x, len(A))
    # nhb = nhbs[random.choice(range(0, len(nhbs)))]
    nhb = random.choice(xrange(0, len(A))) # choose from all points

    delta = A[nhb] - A[x]

    if delta < 0:
        return nhb
    else:
        p = math.exp(-delta / T)
        return nhb if random.random() < p else x

def simulated_annealing(A):
    L = len(A)
    x0 = random.choice(xrange(0, L))
    T = 1.
    k = 1

    x = x0
    x_best = x0

    while T > 1e-3:
        x = make_move(x, A, T)
        if(A[x] < A[x_best]):
            x_best = x
        T = update_temperature(T, k)
        k += 1

    return x, x_best, x0
