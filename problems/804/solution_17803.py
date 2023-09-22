def filtra_pares(a,b,c,d):
    num=(a,b,c,d)
    
    if num[0]%2==0:
        w=num[0]
        return w
    
    elif num[2]%2==0:
        x=num[2]
        return x
    
    elif num[4]%2==0:
        y=num[4]
        return y
    
    elif num[6]%2==0:
        z=num[6]
        return z

        return w,x,y,z