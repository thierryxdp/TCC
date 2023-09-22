def insere(lista_numero,n):
    """A função retorna uma lista ordenada(crescente) e coloca um n
    na ordem certa dentro lista
    list--int-->list"""
    lista_numero.insert(0,n)
    list.sort(lista_numero)
    return lista_numero