A, B =input().split()
H = int(A)
M = int(B)

if H == 0 and M >= 45 : 
    M2 = M - 45
    print(H, M2)

if H == 0 and M < 45 : 
    H2 = H + 23
    M2 = 60 + M - 45
    print(H2, M2)
    
if 0 < H < 24 and M >= 45 :
    M2 = M - 45
    print(H, M2)
    
if 0 < H < 24 and M < 45 : 
    H2 = H - 1
    M2 = 60 + M - 45
    print(H2, M2)