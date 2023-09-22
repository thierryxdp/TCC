def faltante(lista):
    i=0
    peca=0
    while i<len(lista):
        if i not in lista:
            peca=lista[i]
        i=i+1
    return peca