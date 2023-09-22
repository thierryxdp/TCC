def filtra_pares(a,b,c,d):
    if (a//2)==0:
        if (b//2)==0:
            if (c//2)==0:
                if(d//2)==0:
                    return (a,b,c,d)
                else:
                    return (a,b,c)
            else:
                return (a,b)
        else:
            return(a,)
        
    if (b//2)==0:
        if (c//2)==0:
            if (d//2)==0:
                if(a//2)==0:
                    return (a,b,c,d)
                else:
                    return (b,c,d)
            else:
                return (b,c)
        else:
            return(b,)
        
    if (c//2)==0:
        if (d//2)==0:
            if (b//2)==0:
                if(a//2)==0:
                    return (a,b,c,d)
                else:
                    return (b,c,d)
            else:
                return (c,d)
        else:
            return(c,)
        
    if (d//2)==0:
        if (c//2)==0:
            if (b//2)==0:
                if(a//2)==0:
                    return (a,b,c,d)
                else:
                    return (b,c,d)
            else:
                return (c,d)
        else:
            return(d,)
    if (a//2)!=0 and (b//2)!=0 and (c//2)!=0 and (d//2)!=0:
        return ()