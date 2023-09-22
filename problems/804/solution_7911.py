def filtra_pares(a):
    v = [a]
    tupla=tuple(v)
    v.clear()
    tam=len(tupla)
    for i in range(tam):
        if tupla[i]%2==0:
            v.append(tupla[i])
    tupla = tuple(v)
    return(tupla)