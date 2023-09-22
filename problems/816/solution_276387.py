def maiores(numeros, n):
    ordenada =list()
    for c in numeros:
        if(c > n):
            ordenada.append(c)
            ordenada.sort()
            return ordenada
        else:
            return ordenada