def insere(lista_numero,n):
    '''Dada uma lista de números inteiros e um número n, 
    retorna a a lista em ordem crescente e com n inserido.
    list , int -> list'''
    return list.sort(lista_numero+[n])