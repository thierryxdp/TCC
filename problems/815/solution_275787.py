def insere(lista_numero, n):
    """Função que insere um número em uma lista ordenada, mantendo a lista ordenada.
    list,int -> list"""
    lista_numero.append(n)
    return sorted(lista_numero)