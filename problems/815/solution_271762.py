def insere(lista_numero,n):
    '''Dada uma lista de números inteiros e um número n, 
    retorna a a lista em ordem crescente e com n inserido.
    list , int -> list'''
    lista_odern = list.sort(lista_numero+[n])
    return lista_orden