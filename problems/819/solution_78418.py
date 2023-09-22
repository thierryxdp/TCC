def filtraMultiplos(L,N):
    CT = 0
    F = []
    while CT < len(L):
        if L[CT] % N == 0:
            LT = L[N]
        	F = F + [LT]
        CT = CT + 1
    return F