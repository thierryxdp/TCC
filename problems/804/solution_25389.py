def filtra_pares(a,b,c,d):
    """retorna somente os elemetos pares de uma tupla, int,int,int,int -> tupla"""
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    if a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return (a,b,c)
    if a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        return (a,b,d)
    if a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return (a,c,d)
    if a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return (b,c,d)
    if a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return (a,b)
    if a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return (a,c)
    if a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return (b,c)
    if a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return (a,d)
    if a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return (b,d)
    if a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return (c,d)
    if a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:
        return ("")