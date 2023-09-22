def filtra_pares(a==int,b==int,c==int,d==int):
    """calcula e retorna uma tupla contendo apenas numeros pares
    int,int,int,int->int,int,int,int"""
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return a,b,c,d
    if a%2 is not 0 and b%2==0 and c%2==0 and d%2==0:
        return b,c,d
    if a%2==0 and b%2 is not 0 and c%2==0 and d%2==0:
        return a,c,d
    if a%2==0 and b%2==0 and c%2 is not 0 and d%2==0:
        return a,b,d
    if a%2==0 and b%2==0 and c%2==0 and d%2 is not 0:
        return a,b,c
    if a%2 is not 0 and b%2 is not 0 and c%2==0 and d%2==0:
        return c,d
    if a%2 is not 0 and b%2==0 and c%2 is not 0 and d%2==0:
        return b,d
    if a%2 is not 0 and b%2==0 and c%2==0 and d%2 is not 0:
        return b,c
    if a%2==0 and b%2 is not 0 and c%2 is not 0 and d%2==0:
        return a,d
    if a%2==0 and b%2 is not 0 and c%2==0 and d%2 is not 0:
        return a,c
    if a%2==0 and b%2==0 and c%2 is not 0 and d%2 is not 0:
        return a,b
    if a%2==0 and b%2 is not 0 and c%2 is not 0 and d%2 is not 0:
        return a
    if a%2 is not 0 and b%2==0 and c%2 is not 0 and d%2 is not 0:
        return b
    if a%2 is not 0 and b%2 is not 0 and c%2==0 and d%2 is not 0:
        return c
    if a%2 is not 0 and b%2 is not 0 and c%2 is not 0 and d%2==0:
        return d