def filtraMultiplos(lista,n):
    index=0
    lista=[0,1,2,3,4]
    while index<len(lista):
        elemento=lista[index]
        if elemento%n==0:
            return [elemento]
        else:
            return []
        index+=1