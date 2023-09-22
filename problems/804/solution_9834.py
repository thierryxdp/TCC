def filtra_pares(t):
    '''Recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla riginal, na mesma ordem da original; tupla(int, int, int, int) -> tupla'''
    a, b, c, d = t[0], t[1], t[2], t[3]
    a1, b1, c1, d1 = (a % 2), (b % 2), (c % 2), (d % 2)
    if (a1 == 0) and (b1 == 0) and (c1 == 0) and (d1 == 0):
        return (t[0], t[1], t[2], t[3])
    elif (a1 == 0) and (b1 == 0) and (c1 == 0) and (d1 != 0):
        return (t[0], t[1], t[2])
    elif (a1 == 0) and (b1 == 0) and (c1 != 0) and (d1 == 0):
        return (t[0], t[1], t[3])
    elif (a1 == 0) and (b1 != 0) and (c1 == 0) and (d1 == 0):
         return (t[0], t[2], t[3])
    elif (a1 != 0) and (b1 == 0) and (c1 == 0) and (d1 == 0):
        return (t[1], t[2], t[3])
    elif (a1 == 0) and (b1 == 0) and (c1 != 0) and (d1 != 0):
        return (t[0], t[1])
    elif (a1 == 0) and (b1 != 0) and (c1 != 0) and (d1 == 0):
        return (t[0],t[3])
    elif (a1 == 0) and (b1 != 0) and (c1 == 0) and (d1 != 0):
        return (t[0],t[2])
    elif (a1 != 0) and (b1 != 0) and (c1 == 0) and (d1 == 0):
        return (t[2], t[3])
    elif (a1 != 0) and (b1 == 0) and (c1 != 0) and (d1 == 0):
        return (t[1], t[3])
    elif (a1 != 0) and (b1 == 0) and (c1 == 0) and (d1 != 0):
        return (t[1],t[2])
    elif (a1 == 0) and (b1 != 0) and (c1 != 0) and (d1 != 0):
        return (t[0],)
    elif (a1 != 0) and (b1 == 0) and (c1 != 0) and (d1 != 0):
        return (t[1],)
    elif (a1 != 0) and (b1 != 0) and (c1 == 0) and (d1 != 0):
        return (t[2],)
    elif (a1 != 0) and (b1 != 0) and (c1 != 0) and (d1 == 0):
        return (t[3],)
    elif (a1 != 0) and (b1 != 0) and (c1 != 0) and (d1 != 0):
        return ()