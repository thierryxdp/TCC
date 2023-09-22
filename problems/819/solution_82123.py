def filtraMultiplos(listanum,n):
    i=0
    lista=[]
    while i<len(listanum):
        if listanum[i]%n==0:
            lista = lista + listanum[i]
        i=i+1
    return lista