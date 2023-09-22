def qtd_divisores(N):
    X = N + 1
    F = 0
    NU = 1
    while NU !=X:
        if X%NU == 0:
            F=F+1
        elif N < 0:
            F=0
    return F