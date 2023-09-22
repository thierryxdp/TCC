def filtra_pares(x,y,z,q):
    """Função que receba uma tupla com quatro elementos inteiros como parâmetro e retorne apenas os elementos pares da tupla originaa"""
    if x//2 or y//2 or z//2 or q//2:
        return(x,y,z,q)
    else:
        if x//2 or y//2 or z//2: 
            return(x,y,z)
        else:
            if x//2 or y//2:
                return (x,y)
            else:
                if x//2:
                    return(x)
                else:
                    if y//2 or z//2 or q//2:
                        return (y,z,q)
                    else:
                        if y//2 or z//2:
                            return(y,z)
                        else:
                            if y//2:
                                return(y)
                            else:
                                if z//2 or q//2:
                                    return(z,q)
                                else:
                                    if z//2:
                                        return(z)
                                    else:
                                        if q//2:
                                            return(q)