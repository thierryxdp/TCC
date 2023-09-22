def filtraMultiplos(lista,n):
    v=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            v=v+lista[1]
            i=i+1
    return v