def maiores(numeros, n):
    list.insert(numeros, 0, n)
    list.sort(numeros)
    return numeros[list.index(numeros, n)+1:]