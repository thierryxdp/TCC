def repetidos(L):
    C0 = 0
    F = 0
    while C0 < len(L):
        C1 = C0 + 1
        if L[C1] == L[C0]:
            F = F + 1
        C0 = C0 + 1
    return F