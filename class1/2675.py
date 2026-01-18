import sys
t=int(sys.stdin.readline())
for _ in range(t):
    r,s=sys.stdin.readline().split()
    print(''.join(c*int(r) for c in s))