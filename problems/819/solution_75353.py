def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i] % n==0:
            return lista
        i=i+1