def filtraMultiplos(lista,n):
    lista1=[]
    cont=0
    while cont<len(lista):
        lista[cont]%n==0
        lista1=lista1+lista[cont]
        cont=cont+1
    return lista1