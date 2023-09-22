def filtra_pares(a,b,c,d):
    """retorna somente os elemetos pares de uma tupla, int,int,int,int -> tupla"""
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        s=(a,b,c,d)
        return s
    if a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        s=(a,b,c)
        return s
    if a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        s=(a,b,d)
        return s
    if a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        s=(a,c,d)
        return s
    if a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        s=(b,c,d)
        return s
    if a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        s=(a,b)
        return s
    if a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        s= (a,c)
        return s
    if a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        s=(b,c)
        return s
    if a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        s=(a,d)
        return s
    if a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        s=(b,d)
        return s
    if a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        s=(c,d)
        return s
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:
        s=()
        return s