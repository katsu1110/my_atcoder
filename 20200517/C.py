import math

if __name__ == '__main__':
    A, B, H, M = map(int, input().split())
    
    minute_passed = float(H) * 60.0 + float(M)
    l = (0.5 * (math.pi / 180.0) * minute_passed) % (2.0 * math.pi)
    s = (6.0 * (math.pi / 180.0) * minute_passed) % (2.0 * math.pi)
    deg = abs(s - l)
    print(format(math.sqrt(B ** 2.0 + A ** 2.0 - 2.0 * A * B * math.cos(deg)), '.20f'))