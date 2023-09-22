def insere(lista_numero,n):
    """Função que insere número na lista e esta se mantem
    ordenada.
    lista,int->lista"""
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero