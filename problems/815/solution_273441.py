def insere(lista_numero,n):
    """Inclui 'n' na posição correta, de tal maneira que
       a lista continue ordenada, dada uma determinada lista.
       list -> list"""
    lista = list.append(lista_numero, n)
    ordem = list.sort(lista)
    return ordem