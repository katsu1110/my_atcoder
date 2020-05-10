import numpy as np
from itertools import product

if __name__ == '__main__':
    T = input().split()
    N = int(T[0])
    M = int(T[1])
    X = int(T[2])
    price = np.zeros(N)
    qual = np.zeros((N, M))
    for n in range(N):
        t = input().split()
        price[n] = int(t[0])
        qual[n, :] = np.array([int(m) for m in t[1:]])

    cost_min = 1e18
    for idx in product([0, 1], repeat=N):
        cost = 0
        t = X * np.ones(M)
        for j in range(N):
            if idx[j] == 1:
                t -= qual[j, :]
                cost += price[j]
        if max(t) <= 0:
            if cost < cost_min:
                cost_min = cost
    if cost_min == 1e18:
        print(-1)
    else:
        print(int(cost_min))