def maiores(lista,n):
    '''
    função que dada uma lista de números inteiros e um inteiro n, retorna outra lista que contenha todos os números da lista original maiores que n ordenados em ordem crescente;
    lista, int -> list
    '''
    lista[0:0] = [n]
    list.sort(lista)
    indice = list.index(lista,n)
    del lista[:indice]
    return lista