T = int(input())

def method1(mynum, coins):
    return 2 * mynum, coins + A

def method2(mynum, coins):
    return 3 * mynum, coins + B

def method3(mynum, coins):
    return 5 * mynum, coins + C

def method4(mynum, coins):
    return mynum+1, coins + D

def method5(mynum, coins):
    return mynum-1, coins + D

for t in range(T):
    mynum = 0
    coins = 0
    N, A, B, C, D = map(int, input().split())
    

