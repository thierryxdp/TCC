def acima_da_media(lista, numero):
    lista = lista + [numero]
    lista = lista.sorted()
    indice = lista.index(numero)
    del (lista[0:numero])
    return lista