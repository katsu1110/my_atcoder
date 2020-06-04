import math
S = list(input().split())
A = int(S[0])
b_int, b_frac = S[1].split(".")
bb = int(b_int) * 100 + int(b_frac)
print(A ** bb // 100)
