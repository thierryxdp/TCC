def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i] % n==0:
            list.insert(l,i,lista[i])
            list.insert(l,i,lista[i])
            return l
        i=i+1