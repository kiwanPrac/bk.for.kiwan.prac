import sys


N = int(sys.stdin.readline())
Star = "*"
Blank = " "

for i in range(1, N + 1):
    print(Blank * (N - i), Star * i , sep='')