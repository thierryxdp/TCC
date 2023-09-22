def maiores (lista :list, n: int) -> list:
    """Retorna uma lista com todos números maiores que n em lista."""
    list.append(lista, n)
    list.sort(lista)
    contador = list.count(lista, n)
    indice = list.index(lista, n) + contador
    lista_final = lista[indice:]
    return lista_final