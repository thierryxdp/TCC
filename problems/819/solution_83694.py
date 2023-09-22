def filtraMultiplos(lista,n):
    """essa função filtrará os múltiplos de um número dados como parametros uma lista de números e um numero divisor
    list,int->list"""
    divisivel=[]
    proximo=0
    while proximo < len(lista):
        if lista[proximo]%n==0:
            divisivel= divisivel+[lista[proximo],]
        proximo =  proximo+1
    return divisivel