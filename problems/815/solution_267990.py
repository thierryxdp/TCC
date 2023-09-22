def insere(lista_numeros, n):
    """função que dada uma lista ordenada de numeros inteiros e um numero
    inteiro n, inclua n na posição correta"""
    numero=[n]
    lista_nova=lista_numeros+numero
    return list.sort(lista_nova)