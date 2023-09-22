def filtra_pares(t):
    elementos = filter(lambda valor:valor % 2 == 0, t)
    return tuple(elementos)