import sys
nums=map(int,sys.stdin.read().split())
differ=[]
total=[differ.append(n%42) for n in nums if n%42 not in differ]
print(len(total))
