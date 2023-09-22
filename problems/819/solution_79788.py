def filtraMultiplos(lista,n):
    divisiveis=[]
    proximo=0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            list.append(divisiveis,proximo) 
        proximo = proximo + 1
    return divisiveis