def filtra_pares(t):
    lista = []
    lista3=[]
    for sub in t[3]:
        if sub%2==0:
            lista.append(sub)
            return tuple(lista)