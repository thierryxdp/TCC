def maiores(lista: list, n:int) -> list:
    """comentário"""
    lista = lista[0]
    z = n[1]
    lista.append(z)
    
    if max(lista) == z:
        return []
    else:
        lista1 = sorted(lista, reverse = True)
        index_n = lista1.index(x)
        return sorted(lista1[: index_n])