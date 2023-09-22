def filtra_pares(a,b,c,d):
    """Função que dado uma tpla contendo 4 elementos inteiros, retorne uma nova tupla contendo apenas os 
    elemntos pares da tupla de entrada"""
    x = (a%2)
    y = (b%2)
    z = (c%2)
    w = (d%2)
    if (x == 0)and(y == 0)and(z == 0)and(w == 0):
        return a,b,c,d
    elif (x != 0)and(y == 0)and(z == 0)and(w == 0):
        return b,c,d
    elif (x == 0)and(y != 0)and(z == 0)and(w == 0):
        return a,c,d
    elif (x == 0)and(y == 0)and(z != 0)and(w == 0):
        return a,b,d
    elif (x == 0)and(y == 0)and(z == 0)and(w != 0):
        return a,b,c
    elif (x != 0)and(y != 0)and(z == 0)and(w == 0):     
        return c,d
    elif (x != 0)and(y == 0)and(z != 0)and(w == 0):
        return b,d
    elif (x != 0)and(y == 0)and(z == 0)and(w != 0):
        return b,c
    elif (x == 0)and(y != 0)and(z != 0)and(w == 0):
        return a,d
    elif (x == 0)and(y != 0)and(z == 0)and(w != 0):
        return a,c
    elif (x == 0)and(y == 0)and(z != 0)and(w != 0):
        return a,b
    elif (x == 0)and(y != 0)and(z != 0)and(w != 0):
        return a
    elif (x != 0)and(y == 0)and(z != 0)and(w != 0):
        return b
    elif (x != 0)and(y != 0)and(z == 0)and(w != 0):
        return c
    else:
        return d