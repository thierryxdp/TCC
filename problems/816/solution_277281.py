def maiores(lista,n):
    '''Função que recebe uma lista de números inteiros e um número inteiro n e retorna uma nova lista contendo todos os números da lista original que são maiores que n'''
    list.sort(lista)
    c=n+1
    f=lista[len(lista)-1]
    l1=list(range(c,f+1))
    return l1