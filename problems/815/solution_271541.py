def insere(lista_numero,n):
    """calcula e retorna n em uma lista ordenada"""
    return list.sort(lista_numero[:n]+n+lista_numero[n:])