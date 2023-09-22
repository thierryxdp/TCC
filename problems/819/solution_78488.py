def filtraMultiplos(lista_de_numeros, n):
    numeros = []
    i = 0
    while i < len(lista_de_numeros):
        if lista_de_numeros[i] % n == 0:
            numeros += [lista_de_numeros[i]]
        i += 1
    return numeros