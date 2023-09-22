def filtra_pares (a):
    '''funcao que recebe uma tupla com quatro elementos inteiros e retorna uma nova apenas com os elementos pares da original
    tupla -> tupla'''
    a[0] = a
    a[1] = b
    a[2] = c
    a[3] = d
    if (a%2, b%2, c%2, d%2) == (0,0,0,0):
        return (a,b,c,d)
    elif (a%2, b%2, c%2, d%2) == (0,0,0,1):
        return (a,b,c)
    elif (a%2, b%2, c%2, d%2) == (0,0,1,1):
        return (a,b)
    elif (a%2, b%2, c%2, d%2) == (0,1,0,1):
        return (a,c)
    elif (a%2, b%2, c%2, d%2) == (1,0,0,1):
        return (b,c)
    elif (a%2, b%2, c%2, d%2) == (0,1,1,1):
        return (a)
    elif (a%2, b%2, c%2, d%2) == (1,0,1,1):
        return (b)
    elif (a%2, b%2, c%2, d%2) == (1,1,0,1):
        return (c)
    elif (a%2, b%2, c%2, d%2) == (1,1,1,1):
        return ()
    elif (a%2, b%2, c%2, d%2) == (0,0,1,0):
        return (a,b,d)
    elif (a%2, b%2, c%2, d%2) == (0,1,1,0):
        return (a,d)
    elif (a%2, b%2, c%2, d%2) == (1,0,1,0):
        return (b,d)
    elif (a%2, b%2, c%2, d%2) == (1,1,1,0):
        return (d)
    elif (a%2, b%2, c%2, d%2) == (0,1,0,0):
        return (a,c,d)
    elif (a%2, b%2, c%2, d%2) == (1,1,0,0):
        return (c,d)
    elif (a%2, b%2, c%2, d%2) == (1,0,0,0):
        return (a)