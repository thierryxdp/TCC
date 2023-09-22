def filtra_pares(tup):
    lista1=[]
    lista = []
    lista3=[]
    lista4=[]
    for e in tup[:] :
        if e % 2 == 0:
            lista.append(e)
            return tuple(lista)