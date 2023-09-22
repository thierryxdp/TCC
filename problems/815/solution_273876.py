def insere(lista_numero, n):
    """
    Insere um inteiro (n) dentro de uma lista (lista_numero)
    e retorna ela ordenada crescentemente
    """
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero