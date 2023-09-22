def filtra_pares(a, b, c, d):
    """funcao que recebe quatro elementos e retoma uma nova tupla contendo apenas os elementos pares da tupla original."""
    a=t[0]
    b=t[1]
    c=[2]
    d=[3]
    if a%2==0:
        if b%2==0:
            if c%2==0:
                if d%2==0:
                    return (a,b,c,d)
                else:
                    if b%2==0:
                        if c%2==0:
                            if d%2==0:
                                if a%2!=0:
                                    return (b,c,d)
                                else:
                                    if a%2==0:
                                        if c%2==0:
                                            if d%2==0:
                                                if b%2!=0:
                                                    return (a,c,d)
                                                else:
                                                    if a%2==0:
                                                        if b%==0:
                                                            if c%2!=0:
                                                                if d%2==0:
                                                                    return (a,b,d)
                                                                else:
                                                                    if a%2==0:
                                                                        if b%2==0:
                                                                            if c%2==0:
                                                                                if d%2!=0:
                                                                                    return (a,b,c)