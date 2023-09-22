def insere(lista_numero,n):
    '''função que, dada uma lista ordenada (crescente)
    de números inteiros e um número inteiro n, inclui 
    n na posição correta, ou seja, de forma que a lista
    continue ordenada
    list, int -> list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero