def faltante(lista):
    for i in range(len(lista)):
        if lista[i] != i+1:
            return i+1
    return len(lista)+1