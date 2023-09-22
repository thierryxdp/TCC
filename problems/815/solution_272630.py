def insere(lista_numero, n):
    """Função que dada uma lista e um número, tenta inserir esse número com ordenamento"""
    """list, int -> list"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero