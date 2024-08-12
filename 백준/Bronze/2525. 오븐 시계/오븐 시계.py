A, B =input().split()
C = input()
H = int(A)
M = int(B)
E = int(C)

Check = H * 60 + M + E

if H >= 0 and Check < 1440:
    H = H + ((M + E) // 60 * 1)
    M = (M + E) % 60
    print(H, M)

if H >= 0 and Check >= 1440:
    H = H + ((M + E) // 60 * 1)
    M = (M + E) % 60
    print(H - 24, M)