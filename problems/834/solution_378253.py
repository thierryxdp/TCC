def media_matriz(m):
    """essa função recebe uma matriz qualquer
    e calcula a média dos números dessa matriz;
    list->int"""
    i = 0
    cont = 0
    for c in m:
        for n in c:
            i += n
            cont += 1
    return round(i/cont,2)