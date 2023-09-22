def insere(lista_numeros, n):
    """função que dada uma lista ordenada de numeros inteiros e um numero
    inteiro n, inclua n na posição correta"""
    numero=str.append(n)
    lista_n=list(numero)
    lista_nova=lista_numeros+lista_n
    return list.sort(lista_nova)