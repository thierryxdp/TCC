def filtra_pares(s):
    """Função que dado uma tula contendo 4 elementos inteiros, retorne uma nova tupla contendo apenascontendo apenas os 
    elemntos pares da tupla de entrada"""
    """tuple -> int"""
    x = (int(s[0])%2)
    y = (int(s[1])%2)
    z = (int(s[2])%2)
    w = (int(s[3])%2)
    if (x == 0)and(y == 0)and(z == 0)and(w == 0):
        return s[0],s[1],s[2],s[3]
    elif (x != 0)and(y == 0)and(z == 0)and(w == 0):
        return s[1],s[2],s[3]
    elif (x == 0)and(y != 0)and(z == 0)and(w == 0):
        return s[0],s[2],s[3]
    elif (x == 0)and(y == 0)and(z != 0)and(w == 0):
        return s[0],s[1],s[3]
    elif (x == 0)and(y == 0)and(z == 0)and(w != 0):
        return s[0],s[2],s[3]
    elif (x != 0)and(y != 0)and(z == 0)and(w == 0):     
        return s[2],s[3]
    elif (x != 0)and(y == 0)and(z != 0)and(w == 0):
        return s[1],s[3]
    elif (x != 0)and(y == 0)and(z == 0)and(w != 0):
        return s[1],s[2]
    elif (x == 0)and(y != 0)and(z != 0)and(w == 0):
        return s[0],s[3]
    elif (x == 0)and(y != 0)and(z == 0)and(w != 0):
        return s[0],s[2]
    elif (x == 0)and(y == 0)and(z != 0)and(w != 0):
        return s[0],s[1]
    elif (x == 0)and(y != 0)and(z != 0)and(w != 0):
        return s[0]
    elif (x != 0)and(y == 0)and(z != 0)and(w != 0):
        return s[1]
    elif (x != 0)and(y != 0)and(z == 0)and(w != 0):
        return s[2]
    elif (x != 0)and(y != 0)and(z != 0)and(w == 0):
        return s[3],
    else:
        return ()