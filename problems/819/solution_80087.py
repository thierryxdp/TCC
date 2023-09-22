def filtraMultiplos(lista,n):
    f=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            f= f+[f[i],]
        i=i+1
    return f