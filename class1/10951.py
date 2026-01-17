import sys
nums=map(int,sys.stdin.read().split())
print('\n'.join(str(a+b) for a,b in zip(nums,nums)))