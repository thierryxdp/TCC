def filtraMultiplos(lista,n):
    lista1=[]
    cont=0
    while lista[0]<len(lista):
        if lista[0]%n==0:
            lista1=lista1+lista[0]
            cont=cont+1
    return lista1