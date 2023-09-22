#Start your python function here
def filtra_pares(t):
    '''
    A função filtra uma tupla com quatro elementos inteiros,
    deixando apenas os que forem par
    (entrada = (int, int, int, int) / saída = tupla)
    '''
    a, b, c, d = t
    b0, b1, b2, b3 = a % 2 == 0, b % 2 == 0, c % 2 == 0, d % 2 == 0
    y = b0 + b1 + b2 + b3
    if y == 4:
        return a, b, c, d
    elif y == 3:
        if b0 == False:
            t = b, c, d
            return t
        elif b1 == False:
            t = a, c, d
            return t
        elif b2 == False:
            t = a, b , d
            return t
        else:
            t = a, b, c
            return t
    elif y == 2:
        if (b0 and b1) == True:
            t = a, b
            return t
        elif (b0 and b2) == True:
            t = a, c
            return t
        elif (b0 and b3) == True:
            t = a, d
            return t
        elif (b1 and b2) == True:
            t = b, c
            return t
        elif (b1 and b3) == True:
            t = b, d
            return t
        else:
            t = c, d
            return t
    elif y == 1:
        if b0 == True:
            t = a,
            return t
        elif b1 == True:
            t = b,
            return t
        elif b2 == True:
            t = c,
            return t
        else:
            t = d,
            return t
    else:
        t = ()
        return t