def maiores(lista, n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha todos os numeros da lista original maiores que n
    lista de inteiro, int -> lista'''
        a = list.index(lista, n)
        b = list.count(n)
        return lista[a+b:]