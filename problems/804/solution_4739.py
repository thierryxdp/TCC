def filtra_pares(a,b,c,d):
    """função que recebe uma tupla com quatro elementos inteiros e retorna uma tupla contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam"""
    if a%2==0:
        return a
    if b%2==0:
        return b
    if c%2==0:
        return c
    if d%2==0:
        return d
    if a and b%2==0:
        return a,b
    if a and c%2==0:
        return a,c
    if a and d%2==0:
        return a,d
    if b and c%2==0:
        return b,c
    if b and d%2==0:
        return b,d
    if c and d%2==0:
        return c,d
    if a and b and c%2==0:
        return a,b,c
    if a and b and d%2==0:
        return a,b,d
    if a and c and d%2==0:
        return a,c,d
    if b and c and d%2==0:
        return b,c,d
    if a and b and c and d%2==0:
        return a,b,c,d