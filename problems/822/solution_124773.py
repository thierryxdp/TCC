def repetidos(lista):
    n = 0
    return [n + 1 for i in range(len(lista)) if lista[i]==lista[i-1]]