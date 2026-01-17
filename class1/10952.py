import sys
nums=map(int,sys.stdin.read().split()[:-2])
print('\n'.join(str(a+b) for a,b in zip(nums,nums)))