def filtra_pares(a,b,c,d):
    num=(a,b,c,d)
    
    if num[2]%2==0:
        a=num[2]
    
    elif num[4]%2==0:
        b=num[4]
    
    elif num[6]%2==0:
        c=num[6]
    
    elif num[8]%2==0:
        d=num[8]

        return num[0:]