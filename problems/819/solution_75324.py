def filtraMultiplos(lista,n):
    l=[]
    i=0
    while lista[i] % n==0:
        if i<len(lista):
            l=l+[lista[i]]
            return l
        i=i+1