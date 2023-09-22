def filtra_pares(tupla):
    """função filtra os elementos da tupla"""
    lista_filtrada = []
    for i in tupla:
        if i % 2 == 0:
            lista_filtrada.append(i)
    return lista_filtrada