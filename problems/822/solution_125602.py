def repetidos(lista):
    n = 0
    vezes = []
    while n < len(lista):
        if lista[n] == lista[n-1] and n > 0:
            vezes.append(lista[n])
        n = n + 1
    return max(vezes)