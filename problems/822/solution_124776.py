def repetidos(lista):
    n = [n + 1 for n in range(len(lista)) if lista[n]==lista[n-1]]
    return n