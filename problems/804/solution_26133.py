def filtra_pares(t):
    componentes=filter(lambda valor:valor%2==0, t)
    return tuple(componentes)