import sys
h,m=map(int,sys.stdin.readline().split())
hap=h*60+m-45
print(hap//60%24,hap%60)