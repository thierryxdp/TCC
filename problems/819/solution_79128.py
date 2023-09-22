def filtraMultiplos(lista,n):
    """ Recebe uma lista de entrada e retorna uma outra lista apenas com os numeros da lista original que forem divisíveis por um numero n (usando o while);
    list,int->list """
    lista2=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            lista2=lista2+[lista[proximo]]
        proximo=proximo+1
    return lista2