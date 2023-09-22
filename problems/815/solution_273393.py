def insere(lista_numero,n):
    """Tem como objetivo inserir um número inteiro n em uma
    lista de forma que a lista continue ordenada.
    lista,int > lista"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero