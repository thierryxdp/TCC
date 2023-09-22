def filtraMultiplos(lista,n):
    ''' função que recebe uma lista e um numero (n) e retorna 
    outra lista com todos os elementos da lista original que 
    forem divisiveis por n
    list,int->list
    '''
    divisivel=[]
    proximo=0
    while proximo < len(lista):
        if lista[proximo]%n==0:
            divisivel= divisivel+[lista[proximo],]
        proximo =  proximo+1
    return divisivel