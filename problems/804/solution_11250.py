def filtra_pares (a,b,c,d):
    """ os parâmetros de entrada são do tipo (int, int, int, int).
    o valor de retorno é do tipo tupla"""
    
    if a%2 and  b%2 and c%2 and d%2 == 0:
        return (a,b,c,d)
    if b%2 and c%2 and d%2 == 0:
        return (b,c,d)
    if c%2 and d%2 == 0:
        return (c,d)
    if d%2 == 0:
        return (d)
    if a%2 == 0:
        return (a)
    if b%2 == 0:
        return (b)
    if c%2 == 0:
        return (c)
    if a%2 and c%2 and d%2 == 0:
        return (a,c,d)
    if a%2 and d%2 == 0:
        return (a,d)
    if a%2 and  b%2 == 0:
        return (a,b)
    if b%2 and c%2 == 0:
        return (b,c)
    if a%2 and c%2 == 0:
        return (a,c)
    if b%2 and d%2 == 0:
        return (b,d)
    if a%2 and  b%2 and c%2== 0:
        return (a,b,c)