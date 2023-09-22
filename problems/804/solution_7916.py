def filtra_pares (a,b,c,d):
    v = [43 , 55, 23, 12]
    tupla=tuple(v)
    v.clear()
    tam=len(tupla)
    for i in range(tam):
        if tupla[i]%2==0:
            v.append(tupla[i])
    tupla = tuple(v)
    return(tupla)