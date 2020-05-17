if __name__ == '__main__':
    K = int(input())
    S = input()

    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')