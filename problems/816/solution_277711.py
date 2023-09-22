def maiores(lista,n):
    '''Função que recebe uma lista de números inteiros e um número inteiro n e retorna uma nova lista contendo todos os números da lista original que são maiores que n'''
    if n in lista:
        l1= list.sort(lista)
        l2= lista[list.index(lista,n)+1:]
        return l2