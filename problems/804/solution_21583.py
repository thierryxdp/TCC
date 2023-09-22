def filtra_pares(t):
    lista=[]
    d=t
    for a in range(1,100):
        if a%2==0:
            lista.append(a)
            return tuple(lista)