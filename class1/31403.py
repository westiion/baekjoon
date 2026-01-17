# A,B,C를 각각 수와 문자열로 생각했을 때 A+B-C 출력
import sys
a,b,c=sys.stdin.read().split()
ch=str(int(a)+int(b)-int(c))
n=str(int(a+b)-int(c))
print(f'{ch}\n{n}')
