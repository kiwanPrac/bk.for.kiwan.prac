X, Y, Z = input().split()

A = int(X)
B = int(Y)
C = int(Z)

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)