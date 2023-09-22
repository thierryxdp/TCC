def maiores(numeros, n):
    list.insert(numeros, 0, n)
    list.sort(numeros)
    return list.index(numeros, n)