def filtra_pares(a,b,c,d):
    """tupla de 4 elementos e retorna apenas os numeros pares."""
    if (a%2==0):
        return (a)
    elif (a%2<0):
        return filtra_pares[1:]
    if(a%2>0):
        return filtra_pares[1:]
    else:
        if (b%2==0):
            return (b)
        elif (b%2>0):
            return filtra_pares[0:2:]
        if (b%2<0):
            return filtra_pares[0:1:2]
        else:
            if (c%2==0):
                return (c)
            else:
                if (c%2>0):
                    return filtra_pares[0:2:-1]
                if (c%2<0):
                    return filtra_pares[0:2:-1]
                else:
                    if (d%2==0):
                        return (b)
                    else:
                        if (d%2<0):
                            return filtra_pares[:-1]
                        else:
                            if (d%2<0):
                                return filtra_pares[:-1]
                            return (a,b,c,d)