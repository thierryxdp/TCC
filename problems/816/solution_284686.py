def maiores(lista,n):
    lista2=[]
    for i in lista:
        if i > n:
            lista2.append(i).sort()
    return lista2