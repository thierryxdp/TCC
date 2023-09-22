def filtra_pares(t):
    """funçao que recebe um tupla contendo 4 valores inteiros e
    retorna uma tupla contendo os valores pares da tupla original,
    na mesma ordem tup-> tup"""
    a=t[0]
    b=t[1]
    c=t[2]
    d=t[3]
    if a%2==0:
        if b%2==0:
            if c%2==0:
                if d%2==0:
                    return (a,b,c,d)
                else:
                    return (a,b,c)
                else:
                    if d%2==0:
                        return (a,b,d)
                    else:
                        return (a,b)