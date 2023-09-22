def maiores(lista,n):
    '''Recebe uma lista e um número inteiro n
    e retorna outra lista que tem todos os números da lista
    original maiores que n.
    list,int -> list'''
    nova_lista = []
    for i in lista:
        if i > n:
            nova_lista += [i]
    return sorted(nova_lista)