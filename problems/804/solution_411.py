def filtra_pares (a, b, c, d):
    '''funcao que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    tupla->tupla'''
    if (a%2, b%2, c%2, d%2) == (0, 0, 0, 0):
        return (a, b, c, d)
    elif (a%2, b%2, c%2, d%2) == (0, 0, 0, 1):
        return (a, b, c)
    elif (a%2, b%2, c%2, d%2) == (0, 0, 1, 0):
        return (a, b, d)
    elif (a%2, b%2, c%2, d%2) == (0, 1, 0, 0):
        return (a, c, d)
    elif (a%2, b%2, c%2, d%2) == (1, 0, 0, 0):
        return (b, c, d)
    elif (a%2, b%2, c%2, d%2) == (0, 0, 1, 1):
        return (a,b)
    elif (a%2, b%2, c%2, d%2) == (0, 1, 1, 1):
        return (a)
    elif (a%2, b%2, c%2, d%2) == (1, 1, 1, 1):
        return ()
    elif (a%2, b%2, c%2, d%2) == (1, 1, 0, 0):
        return (a, b)
    elif (a%2, b%2, c%2, d%2) == (1, 1, 1, 0):
        return (d)
    elif (a%2, b%2, c%2, d%2) == (0, 1, 1, 0):
        return (b, c)
    elif (a%2, b%2, c%2, d%2) == (1, 0, 0, 1):
        return (a, d)
    elif (a%2, b%2, c%2, d%2) == (1, 0, 1, 1):
        return (a, c, d)
    elif (a%2, b%2, c%2, d%2) == (1, 1, 0, 1):
        return (a, b, d)
    elif (a%2, b%2, c%2, d%2) == (0, 1, 0, 1):
        return (a, c)