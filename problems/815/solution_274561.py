def insere(lista_numero,n):
    '''função que dada uma lista ordenada de números inteiros e um número inteiro n, inclua n na posição correta;
    list, int -> list'''
    lista_numero.append(n)
    lista1 = lista_numero.sort()
    return lista1