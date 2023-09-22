def faltante(lista):
   
    falta=lista[:]
    falta.sort()
    i=0
    peca=-1
    while i <len(lista):
        if falta[i]==falta+1:
            i=i+1
        else:
            peca=contador+1
            i=i+1
    if peca==-1:
        peca=len(falta)+1
    return peca