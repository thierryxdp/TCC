def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i] % n==0:
            l=l+[lista[i]]
            return l+lista[i] % n==0
        i=i+1