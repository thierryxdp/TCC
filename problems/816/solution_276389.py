def maiores(numeros, n):
    tam = []
    for c in numeros:
        if(c>n):
            print(c)
            tam.append(c)
    tam.sort()
    return tam