A, B, C = map(int, input().split())
K = int(input())

n_magic = 0
while (A >= B) & (n_magic <= K):
    n_magic += 1
    B *= 2

if (A >= B) | (n_magic > K):
    print('No')
else:
    if (n_magic <= K) & (B > A) & (C > B):
        print('Yes')
    else:
        while (B >= C) & (n_magic <= K):
            n_magic += 1
            C *= 2

        if (n_magic <= K) & (C > B):
            print('Yes')
        else:
            print('No')