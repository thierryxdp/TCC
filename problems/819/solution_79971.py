def filtraMultiplos(lista,n):
    divisores=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            divisores=divisores+lista[i]
        i=i+1
        return lista