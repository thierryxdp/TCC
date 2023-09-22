def media_matriz(m):
    """ Dada uma matriz m, não vazia, retorna a média aritmética dos seus números
    list -> float"""
    l = []
    for a in m:
        for b in range(len(m[0])):
            l.append(m[a][b])
    return round(sum(l)/len(l),2)