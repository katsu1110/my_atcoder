N = int(input())
As = list(map(int, input().split()))

wallet = 1000
stock = 0
price = 100000
for n in range(N-1):
    print(n, wallet, stock)
    if As[n+1] > As[n]:
        stock = wallet // As[n]
        wallet -= stock * As[n]
        price = As[n]
    elif As[n+1] < As[n]:
        if (stock > 0) & (As[n] > price):
            wallet += stock * As[n]
            stock = 0
            price = 100000
# if As[-2] < As[-1]:
#     wallet += (wallet // As[-2]) * As[-1]
#     stock = 0
#     print(n+1, wallet, stock)

print(wallet)