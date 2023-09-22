def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            i=i+1
            l.insert(i,lista[i])
            return l