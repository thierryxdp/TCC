def filtra_pares_indice(numeros: tuple) -> tuple:
    pares = list()

    for i in range(len(numeros)):
        if (numeros[i] % 2 == 0):
            pares.append(numeros[i])
    

    return tuple(pares)