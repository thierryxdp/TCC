def maiores(*n):
    """Essa função retorna uma lista com todos os números maiores que n."""
    lista = n[0]
    a = n[1]
    lista.append(a)
    if max(lista) == a:
        return []
    else:
        lista1 = sorted(lista, reverse = True)
        index_n = lista1.index(a)
        return sorted(lista1[: index_n])