def repetidos (lista):
    n = 0

    while n < len(lista):
        if lista[n] == lista[n+1]:
            vezes = n + 1
    return vezes