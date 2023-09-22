def repetidos(lista):
    n = 0
    vezes = []
    while n < len(lista):
        if lista.count(lista[n]) >= 1:
            vezes.append(lista.count(lista[n]))
            n = n + 1
    return max(vezes)