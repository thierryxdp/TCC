def maiores(lista,n):
    lista2=[]
    for x in lista:
        if x > n:
            lista2.append(x)
    list.sort(lista2)
    return lista2