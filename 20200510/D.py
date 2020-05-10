if __name__ == '__main__':
    T = input().split()
    N = int(T[0])
    K = int(T[1])
    As = list(map(int, input().split()))
    k = 0
    city = As[k]
    while k < K - 1:
        city = As[city-1]
        k += 1
    print(city)