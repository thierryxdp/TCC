def repetidos(L):
    CT = 0
    F = 0
    while CT < len(L):
        CP = CT + 1
        if L[CP] == L[CT]:
            F = F + 1     
        CT = CT + 1
    return F