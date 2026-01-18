import sys
word=sys.stdin.readline().rstrip()
for i in range(ord('a'),ord('z')+1):
    print(word.find(chr(i)),end=' ')