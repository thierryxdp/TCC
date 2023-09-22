def media_matriz(x):
    """essa função retorna a média dos elementos de uma matriz;
    list->int"""
    i = 0
    cont = 0
    for v in x:
        for numero in v:
            i = i + numero
            cont = cont + 1
    return round (i/cont,2)