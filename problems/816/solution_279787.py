def maiores(lista,n):
    '''função que recebe uma lista de números inteiros e um
    número ineiro n e retorna outra lista com todos os números
    da lista maiores que n
    list, int -> list'''
    list.sort(lista)
    i = list.index(lista,n)
    c = list.count(lista,n)
    return lista[i+c:]