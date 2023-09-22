def maiores(numeros,n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista que contém todos os números da lista original maiores que n, ordenados em ordem crescente: list,int -> list'''
    numeros.sort()
    lista1 = numeros[list.index(numeros,n):]
    return lista1