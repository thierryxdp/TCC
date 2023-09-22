def faltante(lista):
    i = 1    
    while i < len(lista):
        n = lista[i]
        if i != lista[i - 1]:
            r = (lista[i] - 1)
            i = i + 1
        i = i + 1
    return r