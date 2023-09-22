def repetidos(lista):
    n = [lista[i] for i in range(len(lista)) if lista[i]==lista[i-1]]
    return n