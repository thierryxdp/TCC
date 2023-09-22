def faltante(L):
    cont=0
    N=len(L)+1
    while cont<N:
        if L[cont]==cont+1 or L[cont]==cont+2:
            cont=cont+1
        return cont+1