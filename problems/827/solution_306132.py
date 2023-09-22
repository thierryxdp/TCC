def qtd_divisores(N):
    F = 0
    NU = 1
    while NU != N:
        if N % NU == 0:
            F = F + 1
        NU = NU + 1
    return F