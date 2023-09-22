def filtraMultiplos(lista,n):
    divisivel=[]
    proximo=0
    while proximo =< len lista:
        if lista[proximo]%n==0:
            divisivel= divisivel+[lista[proximo],]
        proximo =  proximo+1
    return divisivel