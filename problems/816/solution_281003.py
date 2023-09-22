def maiores(lista, n):
    """aaaa"""
    
    lista.append(n)
    lista_copia = sorted(lista)
    i = lista_copia.index(n)
    
    if max(lista) == n:
        return []
    elif min(lista) == n:
        lista.remove(n)
        return lista
    else:
        maiores = lista_copia[i:]
        return sorted(maiores)