# n번째 줄에는 별 n개 출력, 하지만 오른쪽을 기준으로 정렬
import sys
n=int(sys.stdin.readline())
stars=[]
for i in range(n-1,-1,-1):
    stars.append(f'{" "*i}{"*"*(n-i)}')
print('\n'.join(stars))