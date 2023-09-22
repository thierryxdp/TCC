def maiores (lista,n):
    '''Retorna uma lista com os elementos maiores que n da lista original
    lista, int->lista'''
    menor =min(lista)
    maior = max(lista)
    lista1 = list(range(menor,n+1))
    lista2 = list(range(menor,n+1))
    unica= (lista1 + lista2)
    return unica