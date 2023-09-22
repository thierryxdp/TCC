def filtraMultiplos(lista,n):
    l=[]
    i=-1
    while i<len(lista):
        i=i+1
        if lista[i]%n==0:
            l.insert(i,lista[i])

    return l