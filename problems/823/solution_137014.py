def faltante(lista):
    """funcao que dada uma lista com n-1 termos
    numerados de 1 a n descubra o numero que falta; list->int"""
    l=lista[:]
    l.sort()
    cont=0
    peca=-1
    while cont<len(l):
        if l[cont]==cont+1:
            cont+=1
        else:
            peca=cont+1
            cont=len(l)
    if peca == -1:
        peca =len(l)+1
    return peca