def faltante(lista):
    lista.sort()
    i = 0
    final = -1
    while i < len(lista):
        if lista[i] == i+1:
            i += 1
    return final