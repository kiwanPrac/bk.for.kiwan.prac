import sys 
N = int(sys.stdin.readline())

x = list(map(int,sys.stdin.readline().split()))
v = int(sys.stdin.readline())
count = x.count(v)
print(count)