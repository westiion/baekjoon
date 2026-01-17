import sys
n=int(sys.stdin.readline())
nums=[]
for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    nums.append(a+b)

print('\n'.join(str(i) for i in nums))