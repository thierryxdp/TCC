def maiores(numeros, n):
    tam = []
    for c in numeros:
        if c>n:
            tam.append(c)
        else:
            tam = []
    tam.sort() 


    return tam