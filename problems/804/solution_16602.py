def filtra_pares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if (num % 2) == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    return pares, impares