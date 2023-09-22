def filtra_pares(tupla):
    '''funcao que filtra somente os elemetnos pares em um tupla
    tupla->tupla'''
    tupla=(x,y,z,t)
    a=x[1]
    b=y[2]
    c=z[3]
    d=t[4]
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
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