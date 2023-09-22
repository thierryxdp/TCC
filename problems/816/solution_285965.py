def maiores(lista,n):
    
    maiores = list( )
    lista.sort()
    for x in lista:
        if x>=n:
            maiores.append(x)
    return maiores