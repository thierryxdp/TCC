def insere(lista_numero, n):
    '''Dada uma lista com números inteiros e um numero 
    inteiro n retorna uma lista ordenada com o número n 
    inserido nela
    list, int -> list'''
    lista_numero.append(n)
    return sorted(lista_numero)