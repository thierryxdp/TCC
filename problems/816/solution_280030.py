def maiores (lista,n):
    '''Retorna uma lista com os elementos maiores que n da lista original
    lista, int->lista'''
    menor =min(lista)
    maior = max(lista)
    lista1 = list(range(n, menor))
    lista2 = list(range(n+1, maior+1))
    unica= list.sort(lista1 + lista2)
    return unica