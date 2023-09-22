def insere(lista_numero,n):
    """função que dada uma lista ordenada e um número inteiro 'n', retorne a lista com o número inserido na ordem correta;list, int --> int"""
    lista_numero= list.sort(lista_numero+[n])
    return lista_numero