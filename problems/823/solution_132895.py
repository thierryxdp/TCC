def faltante(lista):
    i = 1
    list.sort(lista)
    while i < len(lista):
        if lista[i] == lista[i] + 1:
            i = i+1
    return lista[i]