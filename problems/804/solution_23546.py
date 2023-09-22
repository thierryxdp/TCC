def filtra_pares(a):
    lista=[]
    for num in a:
        if num%2==0:
            lista.append(num)
    lista=tuple(lista[:])
    return lista