def maiores(lista,n):
    limite = len(lista)
    i = 0
    while i < limite:
        if lista[i] < n:
            del lista[i]
            limite = limite - 1
            i = i + 1
        else:
            i = i + 1          
    return lista