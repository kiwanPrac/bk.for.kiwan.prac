import sys

while True : 
    try : 
        A, B = map(int,sys.stdin.readline().split())
        C = A + B
        print(C)
    except : 
        break