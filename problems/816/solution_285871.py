def maiores(inteiros,n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, contendo todos os números da lista original maiores que n, ordenadas em ordem crescente; list, int -> list'''
    if inteiros > n:
        return list.sort(inteiros)