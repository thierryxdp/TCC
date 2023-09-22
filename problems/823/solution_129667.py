def faltante(lista):
    lista.sort()
    lista.reverse()
    pecas = len(lista)+1
    if 1 not in lista:
        return 1
    for i in lista:
        if i != pecas:
            return i+1
        pecas -= 1