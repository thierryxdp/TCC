def maiores(lista, n):
    '''Função que dada uma lista de números
    inteiros e um número inteiro n, retorna
    uma lista que tenha todos os números
    da lista original que são maiores que n.'''
    list.append(lista,n)
    list.sort(lista)
    indice = list.index(lista,n)
    lista1 = lista[indice + 1:]
    return lista1