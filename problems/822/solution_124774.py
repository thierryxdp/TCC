def repetidos(lista):
    n = 0
    [n + 1 for i in range(len(lista)) if lista[i]==lista[i-1]]
    return n