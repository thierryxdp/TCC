def maiores(lista, n):
    '''Função que recebe uma lista de inteiros e um número inteiro n e retorna outra lista
    com todos os números da lista original maiores que n; list, int -> list'''
    
    list.sort(lista)

    return lista[list.index(lista, n)+1:]