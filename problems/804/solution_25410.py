def filtra_pares(s):
    """retorna somente os elemetos pares de uma tupla, tupla -> tupla"""
    a,b,c,d=s
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
    if a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
        s=(d)
        return s
    if a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        s=(c)
        return s
    if a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        s=(b)
        return b
    if a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        s=(a)
        return s
    if a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        s=(c,d)        
        return s             
    if a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:        
        s=()        
        return s