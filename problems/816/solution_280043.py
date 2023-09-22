def maiores (lista, n):
    '''função que recebe lista e um número e retorna os
    números da lista que sejam maior do que aquele dado'''
    lista_maior = []
    for i in lista:
        if i > n:
            lista_maior.append(i)
            lista_maior.sort()
    return lista_maior