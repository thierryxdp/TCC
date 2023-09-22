def maiores(lista, n):
    '''Dada uma lista de numeros inteiros e um numero n, a funcao retorna uma lista com todos os numeros da lista inicial que sejam maiores que n. 
    List, int -> list'''
    lista_copia = lista[:]
    list.append(lista_copia, n)
    list.sort(lista_copia)
    indice_n = list.index(lista_copia, n)
    return lista_copia[indice_n +1:]