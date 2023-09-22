def faltante(lista):
    '''ff'''
 list.sort(lista)
    i= 0
    while i < len(lista):
        if lista[i] != i + 1:
            return i + 1
        i += 1