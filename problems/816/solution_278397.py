def maiores(lista,n):
    '''função que dada uma lista de números inteiros e um inteiro n, retorna uma lista
       com todos os números maiores do que n. list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    list.clear(lista[:n+1])
    return lista