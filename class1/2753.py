# 연도가 주어졌을 때 윤년이면 1 아니면 0

import sys
y=int(sys.stdin.readline())

if y%4==0 and (y%100!=0 or y%400==0):
    print(1)
else:
    print(0)