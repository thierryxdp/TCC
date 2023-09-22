def maiores(numeros, n):
    if n not in numeros:
        numeros.append(n)
    numeros.sort()
    i = list.index(numeros,n)
    return numeros[i+1:]