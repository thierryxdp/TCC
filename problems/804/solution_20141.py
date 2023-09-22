def filtra_pares(x):
    
    a,b,c,d=x
    
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        y=a,b,c,d
        return y    
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        y=a,b,c
        return y
    elif a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        y=a,b,d
        return y
    elif a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        y=a,c,d
        return y
    elif a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        y=b,c,d
        return y
    elif a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        y=b,c
        return y
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        y=b,d
        return y
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        y=c,d
        return y
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
        y=d,
        return y
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        y=c,
        return y
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        y=a,
        return y
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        y=b,
        return y
    elif a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        y=a,b
        return y
    elif a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        y=a,c
        return y
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        y=a,d
        return y
    else:
        y=()
        return y