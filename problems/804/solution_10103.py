def filtra_pares(a,b,c,d):
    """essa funçao retorna uma nova tupla, apenas com os valores pares da tupla original"""
    """entrada: tupla(int, int, int, int)"""
    """saida: tupla(int, int, int, int)"""
    if a%2==0:
        return a
    if b%2==0:
        return b
    if c%2==0:
        return c
    if d%2==0:
        return d
    return(a,b,c,d)