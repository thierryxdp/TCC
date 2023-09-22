def faltante(lista):
   
    falta=lista[:]
    falta.sort()
    cont=0
    peca=-1
    while cont <len(falta):
        if falta[cont]==cont+1:
            cont=cont+1
        else:
            peca=contador+1
            cont= len(falta) 
    if peca==-1:
        peca=len(falta)+1
    return peca