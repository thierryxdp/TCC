def filtra_pares(k):
    k=[[a,b,c,d]]
        if a%2==0 and b%2==0 and c%2==0 and d%2==0:
                return (a,b,c,d)
        if a%2!=0 and b%2==0 and c%2==0 and d%2==0:
                return (b,c,d)
        if a%2==0 and b%2!=0 and c%2==0 and d%2==0:
                return (a,c,d)
        if a%2==0 and b%2==0 and c%2!=0 and d%2==0:
                return (a,b,d)
        if a%2==0 and b%2==0 and c%2==0 and d%2!=0:
                return(a,b,c)
        if a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
                return(c,d)
        if a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
                return(b,d)
        if a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
                return(b,c)
        if a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
                return(a,d)
        if a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
                return(a,c)
        if a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
                return(a,b)
        if a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
                return(d)
        if a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
                return(a)
        if a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
                return(b)
        if a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
                return(c)