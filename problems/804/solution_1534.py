def filtra_pares(tupla):
    '''funcao que filtra somente os elemetnos pares em um tupla
    tupla->tupla'''
    tupla='a','b','c','d'
    a=tupla[1]
    b=tupla[2]
    c=tupla[3]
    d=tupla[4]
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