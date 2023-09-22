def buscapeca(lista):
    i=1
    while i-1<len(lista):
        if i not in lista:
            peca=i
        i=i+1
    return peca