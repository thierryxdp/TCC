def insere(lista_numero,n):
    '''Recebe uma lista ordenada de números inteiros e um número inteiro n, inclui n
na lista de maneira que ela continue crescente.
list, int -> list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero