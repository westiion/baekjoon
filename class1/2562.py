import sys
nums=list(map(int,sys.stdin.read().split()))
max_val=max(nums)
print(f'{max_val}\n{nums.index(max_val)+1}')