def filtraMultiplos(lista,n):
    l=[]
    i=0
    while lista[i]%n==0:
        if lista[i] % n==0:
            l=l+[lista[i]]
            return l
        i=i+1