def maiores(lista_numeros, n):
    """"""
    list.sort(lista_numeros)
    if n in lista_numeros:
        return lista_numeros[list.index(lista_numeros, n):]