def filtra_pares(z):
    lista=[]
    for i in z:
        if i%2==0:
            lista.append(i)
    return (tuple(lista))