def repetidos(lista):
    n = [i + 1 for i in range(len(lista)) if lista[i]==lista[i-1]]
    return n