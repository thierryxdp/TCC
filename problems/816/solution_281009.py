def maiores(lista, n):
    """aaaa"""
    
    lista.append(n)
    lista = sorted(lista)
    i = lista.index(n)
    
    if max(lista) == n:
        return []
    elif min(lista) == n:
        lista.remove(n)
        return (lista)
    else:
        maiores = lista[i+1:]
        return (maiores)