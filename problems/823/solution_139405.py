def faltante(L):
    N=L[-1]+1
    cont=0
    while cont<N:
        if L[cont]==(L[cont+1])-2:
            cont=cont+1
            return L[cont]+1