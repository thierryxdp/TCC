def intercala(lista1, lista2):
    """str str -> lista
    Esse programa irá combinar duas listas diferentes em uma nova lista.
    Usando índices, o programa irá intercalar os valores de cada lista."""
    lista3=lista1+lista2
    lista3[::2]=lista1
    lista3[1::2]=lista2
    return lista3