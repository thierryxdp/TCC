filtraMultiplos(lista,n):
    novalista=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            novalista=novalista+lista[i]
        i=i+1
    return novalista