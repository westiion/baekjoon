import sys
input=sys.stdin.readline
n=int(input())
results=[]
for _ in range(n):
    a,b=map(int,input().split())
    results.append(str(a+b))
print('\n'.join(results))
