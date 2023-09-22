def faltante(lista):
    N = len(lista) + 1
    i = 0
    
    while i < len(lista):
        if lista[i+1] != lista[i] + 1:
            list.append(lista,lista[i] + 1)
        i = i + 1
    return lista