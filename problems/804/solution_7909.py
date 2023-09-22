def filtra_pares(a, b):
    v = [a, b, c, d]
    tupla=tuple(v)
    v.clear()
    tam=len(tupla)
    for i in range(tam):
        if tupla[i]%2==0:
            v.append(tupla[i])
    tupla = tuple(v)
    return(tupla)