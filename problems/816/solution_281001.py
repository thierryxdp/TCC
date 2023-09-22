def maiores(lista, n):
    """aaaa"""
    i = lista.index(n)
    lista_copia = sorted(lista)
    
    if max(lista) == n:
        return []
    elif min(lista) == n:
        lista.remove(n)
        return lista
    else:
        maiores = lista_copia[i:]
        return maiores