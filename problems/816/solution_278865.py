def maiores(numeros,n):
    list.append(numeros, n)
    list.sort(numeros)
    x = list.index(numeros, n)
    list.remove(numeros, n)
    return numeros[x:]