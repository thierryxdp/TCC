def filtraMultiplos(lista,n):
    i=0
    lista1=[]
    while i<len(lista) and lista[i]%n=0:
        i=i+1
        lista[i]%n=0
        lista1[i]=lista[i]
        return lista1