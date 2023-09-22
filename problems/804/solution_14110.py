def somente_pares(lista_de_numeros):
    lista_filtrada = []
    for i in lista_de_numeros:
        if i % 2 == 0:
            lista_filtrada.append(i)
    return lista_filtrada