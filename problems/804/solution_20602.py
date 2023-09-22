def filtra_pares(x,y,z,w):
    """ função que analisa os quatros 
    números inteiros (x,y,z,w) da tupla 
    original e gera uma nova tupla somente
    com os elementos pares.
    assinatura: int,int,int,int --> tuple
    """
    if x%2==0:
        return x
    else:
        if y%2==0:
            return y
        else:
            if z%2==0:
                return z
            else:
                if w%2==0:
                    return w
                else:
                    return x,y,z,w