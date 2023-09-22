def filtraMultiplos(lista,n):
    lista1=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista=lista + lista[i]
        i=i+1
    return lista