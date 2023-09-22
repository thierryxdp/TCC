def faltante(L):
    cont=0
    N=len(L)+1
    while cont<N:
        if L[cont]==cont+1:
            cont=cont+1
        return cont+1
        if L[cont]==cont+2:
            cont=cont+1
        return cont+1