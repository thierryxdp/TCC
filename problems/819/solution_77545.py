def filtraMultiplos(l,n):
    ''''''
    lista=[]
    f = 0
    while len(l) > l[f]:
        if l[f]%n == 0:
            lista = lista + [l[f]]
        f = f + 1
    return lista