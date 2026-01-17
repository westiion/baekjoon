import sys

N,X=map(int,sys.stdin.readline().split())
nums=map(int,sys.stdin.readline().split())

print(" ".join(str(n) for n in nums if n < X))