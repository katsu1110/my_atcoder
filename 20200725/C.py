N, K = map(int, input().split())
As = list(map(int, input().split()))

for i in range(N-K):
    if As[K+i] > As[i]:
        print('Yes')
    else:
        print('No')