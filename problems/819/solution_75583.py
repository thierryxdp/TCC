def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            l.insert(i,lista[i])
            i=i+1
    return l