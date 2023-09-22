def repetidos(lista):
    elemento = lista[0]
    i = 0
    s = 0
    while i < len(elemento):
        if elemento[i] == elemento[i+1]:
            s = s + 1
        i = i + 1
    return s