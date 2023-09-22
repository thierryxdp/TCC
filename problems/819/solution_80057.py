def filtraMultiplos(lista,n):
    f=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista1=list.insert(lista1,i,lista[i])
            i=i+1
    return lista1