def filtraMultiplos(lista,n):
    lista1=[]
    contador=0
    while contador<len(lista):
        if lista[contador]%n==0:
            lista1= lista1+ [lista[contador],]
        contador=contador+1
    return lista1