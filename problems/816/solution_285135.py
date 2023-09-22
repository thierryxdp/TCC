def maiores(lista,n):
    for k in lista:
        if k<n:
            list.remove(lista,k)
            list.sort(lista)
            return lista