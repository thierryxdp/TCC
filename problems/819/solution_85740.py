def filtraMultiplos(l,n):
    lista=[]
    i=0
    while i <= len(l):
        if (l[i]//n)%2 == 0:
        i= i+1
            lista = lista + (l[i], )
        return lista