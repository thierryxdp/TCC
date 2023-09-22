def insere(lista_numero,n):
    """Dada uma lista crescente de números inteiros e um número n, inclua n na posição que a lista continue ordenada"""
    lista_numero+[n]
    list.sort(lista_numero)
    return lista_numero