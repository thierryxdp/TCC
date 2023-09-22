def filtraMultiplos(lista,n):
    l=[]
    i=0
    while lista[i] % n==0:
        i=i+1
        l=l+[lista[i]]
        return l