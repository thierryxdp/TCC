def insere(lista_numero,n):
    ''' função que dado uma lista ordenada (crescente) de números
    inteiros e um número inteiro n, inclua n em uma posição que
    a lista continue ordenada. list, int -> list'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero