def maiores(lista_num, n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna
outra lista, que contenha todos os números da lista original maiores que n
    list, int -> list
    '''
    list.append(lista_num,n)
    list.sort(lista_num)
    pos = list.index(lista,n)
    del lista[:pos]
    list.remove(lista,n)
    return lista