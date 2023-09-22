def filtra_pares(t):
    lista=[]
    for elemento in t:
        if elemento%2==0:
            lista.append(elemento)
    return tuple(lista)