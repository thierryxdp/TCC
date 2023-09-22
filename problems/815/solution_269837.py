def insere(lista_numero,n):
    """funcao que insere um numero em uma lista crescente e permanece crescente a lista;lista->lista"""
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero