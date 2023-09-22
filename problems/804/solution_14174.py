def filtra_pares(tupla):
    lista_filtrada = 0
    for i in tupla:
        if i % 2 == 0:
            lista_filtrada.append(i)
    return lista_filtrada