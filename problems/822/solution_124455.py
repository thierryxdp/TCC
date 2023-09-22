def repetidos(L):
    CT = 1
    F = 0
    X = len(L)
    while CT < X:
        CP = CT - 1
        if L[CT] == L[CP]:
            F = F + 1
        CT = CT + 1
    return F