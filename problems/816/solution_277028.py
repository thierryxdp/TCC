def maiores (lista, n):
    '''Funcao que, dada uma lista de numeros inteiros e um numero inteiro n, retorna outra
lista, que contenha todos os números da lista original maiores que n,
list, int -> list'''

    lista1 = list.index (lista,n)
    return lista[lista1+1:]