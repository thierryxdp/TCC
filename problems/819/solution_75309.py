def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        i=i+1
        if lista[i] % n==0:
            l=l+[lista[i]]
            return l