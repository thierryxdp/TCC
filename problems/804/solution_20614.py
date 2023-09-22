def filtra_pares(x,y,z,w):
    """ função que analisa os quatros 
    números inteiros (x,y,z,w) da tupla 
    original e gera uma nova tupla somente
    com os elementos pares.
    assinatura: int,int,int,int --> tuple
    """
    if x%2==0 and y%2==0 and z%2==0 and w%2==0:
        return x,y,z,w
    else:
        if x%2 ==0 or y%2==0 or z%2==0:
            return (x,y,z)