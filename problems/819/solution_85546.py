def filtraMultiplos(x,n):
    lista=[]
    for r in x:
        if r%n == 0:
            lista.append(r)
    return lista