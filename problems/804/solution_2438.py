def filtra_pares(a):
    
    if a[0]%2==0 and a[1]%2==0 and a[2]%2==0 and a[3]%2==0:
         return (a[0],a[1],a[2],a[3])
    elif a[0]%2==0 and a[1]%2==0 and a[2]%2==0 and a[3]%2!=0:
        return (a[0],a[1],a[2],)
    elif a[0]%2==0 and a[1]%2==0 and a[2]%2!=0 and a[3]%2==0:
        return (a[0],a[1],a[3])
    elif a[0]%2==0 and a[1]%2!=0 and a[2]%2==0 and a[3]%2==0:
        return (a[0],a[2],a[3])
    elif a[0]%2!=0 and a[1]%2==0 and a[2]%2==0 and a[3]%2==0:
        return (a[1],a[2],a[3])
    elif a[0]%2==0 and a[1]%2!=0 and a[2]%2!=0 and a[3]%2==0:
        return (a[0],a[3])
    elif a[0]%2==0 and a[1]%2!=0 and a[2]%2==0 and a[3]%2!=0:
        return (a[0],a[2])
    elif a[0]%2==0 and a[1]%2==0 and a[2]%2!=0 and a[3]%2!=0:
        return (a[0],a[1])
    
    
    
    
    else:
        return ()