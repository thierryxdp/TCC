def qtd_divisores(N):
    X = N + 1
    F = 0
    NU = 1
    while NU != X:
        if X % NU == 0:
            F = F + 1
        NU = NU + 1
    return F