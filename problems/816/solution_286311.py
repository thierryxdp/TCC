def maiores(lista,n):
    limite = len(lista)
    i = 0
    while i < limite:
        if lista[i] < n:
            del lista[i]
    i = i + 1
    limite = limite - 1
    return lista