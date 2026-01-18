import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    ox=input().rstrip().split('X')
    score=sum(len(o)*(len(o)+1)//2 for o in ox)
    print(score)
