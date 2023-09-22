def maiores(lista,n):
    '''Dada uma lista de numeros inteiros e um inteiro n,
    retorna uma lista que contenha os numeros da lista
    original que são maiores que n, ordenados de forma
    crescente; list, int -> list'''
    lista_nova = lista
    list.append(lista_nova,n)
    list.sort(lista_nova)
    inicio = list.index(lista_nova,n)
    return lista_nova[(inicio+1):]