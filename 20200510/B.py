if __name__ == '__main__':
    S = input().split()
    A = int(S[0])
    B = int(S[1])
    C = int(S[2])
    K = int(S[-1])

    if K <= A:
        print(K)
    elif K > A:
        if A + B >= K:
            print(A)
        elif A + B < K:
            print(2*A+B-K)