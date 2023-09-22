def filtra_pares(s):
    """Função que dado uma tula contendo 4 elementos inteiros, retorne uma nova tupla contendo apenascontendo apenas os 
    elemntos pares da tupla de entrada"""
    """tuple -> int"""
    x = (int(s[0])%2)
    y = (int(s[1])%2)
    z = (int(s[2])%2)
    w = (int(s[3])%2)
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