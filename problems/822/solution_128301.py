def repetidos(N):
    repete = 0
    r = 0
    for numeros in N:
        if numeros == N[r-1]:
            repete = repete + 1
            r = r + 1
        else:
            r = r + 1
    return repete