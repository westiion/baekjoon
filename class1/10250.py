import sys
input=sys.stdin.readline
case=int(input())
for _ in range(case):
    h,w,n=map(int,input().split())
    front=(n-1)%h+1
    back=(n-1)//h+1
    print(front*100+back)