def filtra_pares(a,b,c,d):
    """recebe uma tupla de quatro elementos e retorna uma tupla com os elementos pares da tupla de entrada na mesma ordem; int, int, int, int -> tupla"""
    if a//2==0 and b//2==0 and c//2==0 and d//2==0:
        return (a,b,c,d)
    elif a//2==0 and b//2==0 and c//2==0 and d//2!=0:
        return (a,b,c)
    elif a//2==0 and b//2==0 and c//2!=0 and d//2==0:
        return (a,b,d)
    elif a//2==0 and b//2==0 and c//2!=0 and d//2!=0:
        return (a,b)
    elif a//2==0 and b//2!=0 and c//2==0 and d//2==0:
        return (a,c,d)
    elif a//2==0 and b//2!=0 and c//2==0 and d//2!=0:
        return (a,c)
    elif a//2==0 and b//2!=0 and c//2!=0 and d//2==0:
        return (a,d)
    elif a//2==0 and b//2!=0 and c//2!=0 and d//2!=0:
        return (a)
    elif a//2!=0 and b//2==0 and c//2==0 and d//2==0:
        return (b,c,d)
    elif a//2!=0 and b//2==0 and c//2==0 and d//2!=0:
        return (b,c)
    elif a//2!=0 and b//2==0 and c//2!=0 and d//2==0:
        return (b,d)
    elif a//2!=0 and b//2==0 and c//2!=0 and d//2!=0:
        return (b)
    elif a//2!=0 and b//2!=0 and c//2==0 and d//2==0:
        return (c,d)
    elif a//2!=0 and b//2!=0 and c//2==0 and d//2!=0:
        return (c)
    else a//2!=0 and b//2!=0 and c//2!=0 and d//2==0
        return (d)