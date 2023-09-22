def qtd_divisores(N):
    F = 0
    NU = 1
    if N < 0:
        return 0
    while NU != N:
        if N % NU == 0:
            F = F + 1
        NU = NU + 1
        
    return F + 1