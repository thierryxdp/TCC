def filtra_pares(a):
    """Dados 4 numeros inteiros essa funcao retorna os numeros pares dentro
    desses 4 numeros
    """
    if int(a[0]%2==0) and int(a[1]%2==0) and int(a[2]%2==0) and int(a[3]%2==0):
        return (a)
    elif a[0]%2==0 and b[0]%2==0 and c[0]%2==0:
        return (a,b,c)
    elif a%2==0 and b%2==0 and d%2==0:
        return (a,b,d)
    elif a%2==0 and c%2==0 and d%2==0:
        return (a,c,d)
    elif b%2==0 and c%2==0 and d%2==0:
        return (b,c,d)
    elif a%2==0 and b%2==0:
        return (a,b)
    elif a%2==0 and c%2==0:
        return (a,c)
    elif a%2==0 and d%2==0:
        return (a,d)
    elif b%2==0 and c%2==0:
        return (b,c)
    elif b%2==0 and d%2==0:
        return (b,d)
    elif c%2==0 and d%2==0:
        return (c,d)
    elif a%2==0:
        return (a)
    elif b%2==0:
        return (b)
    elif c%2==0:
        return (c)
    elif d%2==0:
        return (d)
    else:
        return print('()')