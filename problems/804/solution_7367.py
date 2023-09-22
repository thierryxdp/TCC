def filtra_pares(s):
    """Função que dado uma tpla contendo 4 elementos inteiros, retorne uma nova tupla contendo apenas os 
    elemntos pares da tupla de entrada"""
    x = int(s[0])//2
    y = int(s[1])//2
    z = int(s[2])//2
    w = int(s[3])//2
    if (x == 0)and(y == 0)and(z == 0)and(w == 0):
        return x,y,z,w
    elif (x != 0)and(y == 0)and(z == 0)and(w == 0):
        return y,z,w
    elif (x == 0)and(y != 0)and(z == 0)and(w == 0):
        return x,z,w
    elif (x == 0)and(y == 0)and(z != 0)and(w == 0):
        return x,y,w
    elif (x == 0)and(y == 0)and(z == 0)and(w != 0):
        return x,y,z
    elif (x != 0)and(y != 0)and(z == 0)and(w == 0):     
        return z,w
    elif (x != 0)and(y == 0)and(z != 0)and(w == 0):
        return y,w
    elif (x != 0)and(y == 0)and(z == 0)and(w != 0):
        return y,z
    elif (x == 0)and(y != 0)and(z != 0)and(w == 0):
        return x,w
    elif (x == 0)and(y != 0)and(z == 0)and(w != 0):
        return x,z
    elif (x == 0)and(y == 0)and(z != 0)and(w != 0):
        return x,y
    elif (x == 0)and(y != 0)and(z != 0)and(w != 0):
        return x
    elif (x != 0)and(y == 0)and(z != 0)and(w != 0):
        return y
    elif (x != 0)and(y != 0)and(z == 0)and(w != 0):
        return z
    elif (x != 0)and(y != 0)and(z != 0)and(w == 0):
        return w