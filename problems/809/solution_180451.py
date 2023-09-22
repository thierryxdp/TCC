def intercala(lista1,lista2):
    lista = lista1 + lista2
    lista[::2] = lista1
    lista[1::2] = lista2
    return lista