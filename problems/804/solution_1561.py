def filtra_pares(tupla):
    '''funcao que filtra somente os elemetnos pares em um tupla
    tupla->tupla'''
    tupla=str
    a=int(tupla[0:1])
    b=int(tupla[2:3])
    c=int(tupla[4:5])
    d=int(tupla[6:7])
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return lista(a,b,c,d)
    elif b%2==0 and a%2!=0 and c%2!=0 and d%2!=0:
        return (b,)
    elif c%2==0 and a%2!=0 and b%2!=0 and d%2!=0:
        return (c,)
    elif d%2==0 and a%2!=0 and b%2!=0 and c%2!=0:
        return (d,)
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        return (a,)
    elif a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return (a,b,)
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return (a,b,c,)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return (a,c,)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return (a,c,d,)
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return (a,d,)
    else:
        return ()