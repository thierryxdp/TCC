def maiores (lista, n):
    """ retorna uma lista com os numeros maiores que n em ordem crescente."""
    list.sort(lista)
    a = list.index(lista, n)
    lista2 = lista[a-1:]
    return lista2