def maiores(lista, n):
    '''Dada uma lista de numeros inteiros e um numero n, a funcao retorna uma lista com todos os numeros da lista inicial que sejam maiores que n. 
    List, int -> list'''
    list.append(lista, n)
    list.sort(lista)
    indice_n = list.index(lista, n)
    return lista[indice_n +1:]