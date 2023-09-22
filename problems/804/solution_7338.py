def filtra_pares(a, b, c, d,):
    """Função que dado uma tpla contendo 4 elementos inteiros, retorne uma nova tupla contendo apenas os 
    elemntos pares da tupla de entrada"""
    x = a//2
    y = b//2
    z = c//2
    w = d//2
    if (x,y,z,w) == 0:
        return (x,y,z,w)
    elif (y,z,w)==0:
        return (y,z,w)
    elif (x,z,w)==0:
        return (x,z,w)
    elif (x,y,w)==0:
        return (x,y,w)
    elif (x,y,z)==0:
        return (x,y,z)