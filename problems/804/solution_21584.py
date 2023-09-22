def filtra_pares(t):
    lista=[]
    d=t
    for a in range(t[0],t[-1]):
        if a%2==0:
            lista.append(a)
            return tuple(lista)