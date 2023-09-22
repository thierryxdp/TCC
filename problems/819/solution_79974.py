def filtraMultiplos(lista,n):
    divisores=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            append(lista[i],divisores)
        i=i+1
        return lista