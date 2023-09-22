def filtraMultiplos(lista,n):
    lista1=[]
    i=0
    while lista[i]%n==0:
        list.insert(lista1,i,lista[i])
        i=i+1
        return lista1