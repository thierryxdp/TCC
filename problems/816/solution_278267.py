def maiores(lista, n):
    '''Função que dada uma lista de números inteiros e um número
    inteiro n retorna outra lista apenas com os números da lista 
    fornecida que são maiores que o inteiro n fornecido. list, int -> list'''
    nova_lista = list.sort(lista)
    x = list.index(nova_lista, n)
    return nova_lista[x:-1]