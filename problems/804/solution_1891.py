def filtra_pares(a,b,c,d):
    """Função que recebe como entrada uma tupla com quatro elementos inteiros, e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que estavam."""
    if a%2==0 and b%2==0 and c%2==0:
        return (a,b,c)
    elif a%2==0 and c%2==0:
        return (a,c)
    elif a%2==0 and b%2==0:
        return (a,b)
    elif d%2==0:
        return (d)
    elif a%2==0 and c%2==0 and d%2==0:
        return (a,c,d)
    elif a%2==0 and b%2==0 and c%2==0:
        return (a,b,c)
    elif  c%2==0 and d%2==0:
        return (c,d)
    elif b%2==0 and c%2==0:
        return (b,c)
    elif a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    elif a%2==0 and c%2==0 and d%2==0:
        return (a,c,d)
    elif b%2==0 and c%2==0 and d%2==0:
        return (b,c,d)
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:
        return ()