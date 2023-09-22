#Start your python function here
def filtra_pares(tupla):
    v = (tupla)
    tupla=tuple(v)
    tam=len(tupla)
    for i in range(tam):
        if tupla[i]%2==0:
            v.append(tupla[i])
    tupla = tuple(v)
    return(tupla)