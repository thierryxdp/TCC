def maiores(lista, n):
    '''Função que dada uma lista de números inteiros e um número
    inteiro n retorna outra lista apenas com os números da lista 
    fornecida que são maiores que o inteiro n fornecido. list, int -> list'''
    list.insert(lista, 0, n)
    list.sort(lista)
    return lista[(list.index(lista, n))+1:]