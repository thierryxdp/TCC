def filtra_pares(a):
    numeros = [a]
    pares = filter(lambda valor: valor % 2 == 0, numeros)
    return pares