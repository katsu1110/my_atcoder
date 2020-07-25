X = int(input())

S = 400
D = 200
for n in range(8):
    if (S <= X) & (X <= S + D - 1):
        print(str(8-n))
    S += D
     