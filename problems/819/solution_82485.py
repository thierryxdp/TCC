def filtraMultiplos(lista,n):
    multiplos=[]
    indece=0
    while indece<len(lista):
        if lista[indece]%n ==0:
            list.append(multiplos,lista[indece])
        indece=indece+1
    return multiplos