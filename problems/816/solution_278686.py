def maiores(lista, n):
    '''Função que dada uma lista de números
    inteiros e um número inteiro n, retorna
    uma lista que tenha todos os números
    da lista original que são maiores que n.'''
    lista1 = list.append(lista,n)
    lista2 = list.sort(lista1)
    indice = list.index(lista2,n)
    lista3 = lista[indice + 1]
    return lista3