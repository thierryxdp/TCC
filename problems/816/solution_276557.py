def maiores(lista, n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha todos os numeros da lista original maiores que n
    lista de inteiro, int -> lista'''
    list.sort(lista)
    lista_nova = lista + [n]
    x = list.index(lista_nova,n)
    return lista_nova[x:]