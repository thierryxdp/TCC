def maiores(lista,n):
    '''função que recebe uma lista de números inteiros e um
    número ineiro n e retorna outra lista com todos os números
    da lista maiores que n
    list, int -> list'''
    list.sort(lista)
    a = 0
    nova_lista = []
    while a < len(lista):
        if lista[a] > n:
            list.append(nova_lista,lista[a])
        a += 1
    return nova_lista