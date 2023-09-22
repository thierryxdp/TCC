def media_matriz(m):
    """ Dada uma matriz m, não vazia, retorna a média aritmética dos seus números
    list -> float"""
    l = []
    for a in m:
        for b in m[a]:
            l.append(b)
    return round(sum(l)/len(l),2)