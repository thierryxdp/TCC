def insere(lista_numeros, n):
    """função que dada uma lista ordenada de numeros inteiros e um numero
    inteiro n, inclua n na posição correta"""
    lista_nova=lista_numeros+n
    return list.sort(lista_nova)