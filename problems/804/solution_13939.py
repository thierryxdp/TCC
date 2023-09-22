def filtra_pares(a,b,c,d):
    """retorna uma nova tupla contendo apenas os elementos pares da tupla original;
    tuple -> tuple"""
    def par(x):
        return x%2==0
    if par(a) and par(b) and par(c) and par(d):
        return (a,b,c,d)
    else:
        return ()