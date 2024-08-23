N, M = map(int,input().split())
basket = [0] * N

for i in range(N):
    basket[i] = i + 1

for A in range(M):
    i, j = map(int,input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for A in range(N):
    print(basket[A], end = " ")