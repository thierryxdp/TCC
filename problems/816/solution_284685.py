def maiores(lista,n):
    lista2=[]
    for i in lista:
        if i > n:
            lista2.append(i)
            list.sort(lista2)
        else:
            lista2=[]
    return lista2