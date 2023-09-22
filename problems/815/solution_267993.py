def insere(lista_numeros, n):
    """função que dada uma lista ordenada de numeros inteiros e um numero
    inteiro n, inclua n na posição correta"""
    numero=str(n)
    lista_numerica=list(numero)
    lista_nova=lista_numeros+lista_numerica
    return lista_nova