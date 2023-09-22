def maiores(numeros, n):
    tam = []
    for c in numeros:
        if(c>n):
            tam.append(c)
    tam.sort()
    return tam