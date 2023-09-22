def faltante(lista):
    l=lista[:]
    l.sort()
    cont=0
    peca=-1
    while cont <len(l):
        if l[cont]==cont+1:
            cont±1
        else:
            peca = cont+1
            cont=len(l)       
    if peca == -1:
                peca = len(l)+1
                return peca