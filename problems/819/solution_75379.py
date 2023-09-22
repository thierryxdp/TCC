def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i] % n==0:
            lista[%n]=(i,lista[i])
            return lista
        i=i+1