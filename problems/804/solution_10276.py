def filtra_pares(x,y,z,q):
    """Função que receba uma tupla com quatro elementos inteiros como parâmetro e retorne apenas os elementos pares da tupla originaa"""
    if x//2 and y//2 and z//2 and q//2:
        return(x,y,z,q)
    else:
        if x//2 and y//2 and z//2:
            return(x,y,z)
        else:
            if x//2 and y//2:
                return (x,y)
            else:
                if x//2:
                    return(x)
                else:
                    if y//2 and z//2:
                        return (y,z)
                    else:
                        if y//2:
                            return(y)
                        else:
                            if z//2:
                                return(z)