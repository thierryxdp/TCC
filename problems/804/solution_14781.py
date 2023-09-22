def filtra_pares(tupla):
    """a função filtra os pares dos impares"""
    lista_filtrada = []
    for i in tupla:
        if i % 2 == 0:
            lista_filtrada.append(i)
    return tuple(lista_filtrada)