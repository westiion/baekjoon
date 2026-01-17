# 공백 없이 쓰인 n개의 숫자 합

import sys
n,numbers=sys.stdin.read().split()
numbers=numbers[:int(n)]
result=sum(map(int,numbers))
print(result)