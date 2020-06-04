N = int(input())
As = list(map(int, input().split()))
if 0 in As:
    print(0)
else:
    As = sorted(As, reverse=True)
    ans = 1
    break_flag = 0
    for n in range(N):
        ans *= As[n]
        if ans > 1e18:
            print(-1)
            break_flag = 1
            break
    if break_flag == 0:
        print(ans)