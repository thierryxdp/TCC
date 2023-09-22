def repetidos(N):
    repete = 0
    r = 1
    for numeros in N:
        if numeros == N[r]:
            repete = repete + 1
            r = r + 1
        else:
            r = r + 1
    return repete