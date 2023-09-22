def insere(lista_numero,n):
    '''função que dada uma lista ordenada de números
    inteiros e um numero inteiro, retorne o numero
    dado na posição correta na lista
    list, int -> list'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero