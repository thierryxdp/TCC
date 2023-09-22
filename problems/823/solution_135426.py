def faltante(lista):
    lista1=lista[:]
    lista.sort()
    i=0
    peca=-1
    while len(lista1)>i:
        if lista1[i]==i+1:
            i=i+1
        else:
            peca=i+1
            i=i+1
        return i
    if peca==-1:
        peca=len(lista1)+1
    return peca