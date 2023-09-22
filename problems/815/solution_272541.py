def insere(lista_numero,n):
    """ Dada um lista ordenada de numeros inteiros e um número inteiro n, insere n em uma posição onde a lista permanece ordenadada.
    list->int"""
    a=lista_numero
    b=[n]
    lista=a+b
    return list.sort(lista)