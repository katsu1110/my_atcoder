"""
multi-input example

EXAMPLE:
cat input_text.txt | python3 multi_input.py

"""

if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(N):
        s = input()
        L.append(s)
    ans = " ".join(L)
    print(ans)