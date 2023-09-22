def maiores(lista, n):
    '''Faça uma função que dada uma lista de números inteiros e um número 
    inteiro n, retorna outra lista, que contenha todos os números 
    da lista original maiores que n.'''
    # int > int
    lista.append(n)
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]