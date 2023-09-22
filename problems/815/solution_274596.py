def insere(lista, n):
    '''função que dada uma lista ordenada de números inteiros e um número inteiro n, inclua n na posição correta;
    list, int -> list'''
    lista.append(n)
    list.sort(lista)
    return lista