import sys
a,b,c=map(int,sys.stdin.read().split())
mul=str(a*b*c)
results=[0]*10
for i in mul:
    results[int(i)]+=1
print('\n'.join(map(str,results)))