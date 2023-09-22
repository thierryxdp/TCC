def maiores(lista, n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha todos os numeros da lista original maiores que n
    lista de inteiro, int -> lista'''
    lista = lista + [n,]
    lista = list.sort(lista)
    return lista[n:]