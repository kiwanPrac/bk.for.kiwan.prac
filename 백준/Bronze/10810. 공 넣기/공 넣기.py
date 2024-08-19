N, M = map(int,input().split())
basket = [0] * N

for i in range(M):
    i, j, k = map(int,input().split())
    for B in range(i-1, j):
        basket[B] = k
        
for B in range(N):
    print(basket[B], end=" ")