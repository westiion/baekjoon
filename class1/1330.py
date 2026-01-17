# 두 정수 A와 B가 주어졌을 때, A와 B 비교하기

A,B=map(int,input().split())
if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')
    