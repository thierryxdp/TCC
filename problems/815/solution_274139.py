def insere(lista_numero, n):
    '''Faça uma funçao dada uma lista ordenada de números inteiros e um número inteiro n, inclua n na psição correta, list, int -> list'''
    ordem = list.extend(lista_numero, n)
    ordem.sort()
    return ordem