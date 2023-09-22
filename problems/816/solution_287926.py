def maiores(lista, numero):
    """Retorna uma lista com os números maiores que n da lista fornecida, em ordem crescente.
    list, int -> list"""
    lista.append(numero)
    lista.sort()
    return lista[lista.index(numero) + 1:]