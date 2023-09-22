def maiores(lista, n):
    '''ao receber uma lista de números inteiros
    e um número inteiro n, retorna um lista contendo
    apenas os elementos maiores que o número n inserido.
    list, int -> list'''
    list.append(lista, n)
    list.sort(lista)
    indice = list.index(lista, n)
    del lista[:indice+1]
    return lista