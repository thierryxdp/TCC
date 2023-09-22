def maiores (lista,n):
    '''Retorna uma lista com os elementos maiores que n da lista original
    lista, int->lista'''
    menor =min(lista)
    maior = max(lista)
    lista2 = list(range(n+1,maior))
    l = ' '.join(lista2)
    l2 = ' '.join(lista)
    s = str,strip(l, l2)
    return s