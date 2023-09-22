def maiores(numeros, n):
    ordenada =list()
    for c in numeros:
        if(c > n):
            ordenada.append(c)
            ordenada.sort()
        else:
            return ordenada