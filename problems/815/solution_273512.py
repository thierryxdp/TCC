def insere(lista_numero,n):
    ''' A partir de uma lista em ordem crescente e
    um número inteiro n, inclui n na posição correta,
    fazendo com que a lista continue ordenada.
    list, int -> list'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero