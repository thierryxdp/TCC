def filtraMultiplos(lista,n):
    """ Recebe uma lista de entrada e retorna uma outra lista apenas com os numeros da lista original que forem divisíveis por um numero n;
    list,int->list """
    lista2=[x for x in lista if x%n==0]
    return lista2