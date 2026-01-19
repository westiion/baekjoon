import sys
nums=list(map(int,sys.stdin.readline().split()))
asc=sorted(nums)
dsc=sorted(nums,reverse=True)
if nums == asc:
    print('ascending')
elif nums == dsc:
    print('descending')
else:
    print('mixed')