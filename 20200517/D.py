import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

if __name__ == '__main__':    
    N, M = map(int, input().split())
    p = np.zeros((N, N))
    for m in range(M):
        A, B = map(int, input().split())
        p[A-1, B-1] = 1
        p[B-1, A-1] = 1
    csr = csr_matrix(p)
    _, predecessors = dijkstra(csr, directed=False, indices=0, return_predecessors=True)
    if -9999 in predecessors[1:]:
        print('No')
    else:
        print('Yes')
        for n in range(N-1):
            print(predecessors[n+1]+1)

    
    