def insere(lista_numero, n):
    '''Funcao recebe uma  lista de números inteiros e um numero que eve ser adicionado a essa lista que está de forma crescente
lista/ int -> lista'''
    listaN = (lista_numero + [n])
    list.sort(listaN)
    return listaN