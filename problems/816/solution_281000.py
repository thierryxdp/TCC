def maiores(lista, n):
    """aaaa"""
    i = lista.index(n)
    lista_copia = sorted(lista)
    lista_maiores = []
    if max(lista) == n:
        return []
    elif min(lista) == n:
        lista.remove(n)
        return lista
    elif lista_copia[i-1]