def insere(lista_numero,n):
    '''função que dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue ordenada.
    Entrada: list, int;
    saída: list'''
    return list.sort(list.extend(lista_numero,[n]))