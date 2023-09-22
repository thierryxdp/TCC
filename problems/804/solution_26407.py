def filtra_pares(tupla):
    lista=[]
    for i in tupla:
        if i%2==0:
            lista.append(i)
    return tuple(lista)