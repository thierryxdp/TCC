def maiores(lista, n):
    if n not in lista:
        lista.appen(n)
        lista.sort()
        l= lista.index(n)
        lista2= lista[l+1:]
        rep= lista2.count(n)
        returnlista2[rep:]