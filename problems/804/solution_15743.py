def filtra_pares(a,b,c,d):
    """tupla de 4 elementos e retorna apenas os numeros pares."""
    if (a%2==0):
        return (a)
    else:
        if (a%2>0):
            return filtra_pares[1:]
        else:
            if(a%2<0):
                return filtra_pares[1:]