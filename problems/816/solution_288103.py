def maiores(lista,n):
    
    """list -> list"""
    l = []
    for i in range(len(lista)):
        if lista[i] > n:
            l.append(lista[i])
    l.sort()
    return l