# 검증수

nums=map(int,input().split())
print(sum(i**2 for i in nums)%10)