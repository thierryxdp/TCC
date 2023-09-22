def maiores(lista,n):
    """ Dada uma lista de numeros inteiros, retorna outra lista contendo os numeros da lista original maiores que n;
    list,int->list """
    lista2=[x for x in lista if x>n]
    return lista2