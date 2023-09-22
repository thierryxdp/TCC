def faltante(lista):
    l=lista[:]
    l.sort()
    cont=0
    peca=-1
    while cont <len(1):
        if l[cont]==cont+1:
            cont+=1
        else:
            peca = cont+1
            cont=len(1)
    if peca == -1:
        peca == len(1)+1
    
    return peca