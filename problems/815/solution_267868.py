def insere(lista_numero, n):
    '''função que, dada uma lista ordenada (crescente) de números inteiros e um
    número inteiro n, inclue n na posição correta, ou seja, a lista continua
    ordenada; list, int -> list'''
    lista = lista + [n] 
    list.sort(lista)
    return lista