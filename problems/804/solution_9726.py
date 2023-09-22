def filtra_pares(a,b,c,d):
    if a%2==0:
        if b%2==0:
    		if c%2==0:
                if d%==0:
                    return(a,b,c,d)
               	else:
                    return(a,b,c)
           	else:
                if d%==0:
                    return(a,b,d)
               	else:
                    return(a,b)
        else:
            if c%2==0:
                if d%==0:
                    return(a,c,d)
               	else:
                    return(a,c)
           	else:
                if d%==0:
                    return(a,d)
               	else:
                    return(a)
    
    else:
        if b%2==0:
    		if c%2==0:
                if d%==0:
                    return(b,c,d)
               	else:
                    return(b,c)
           	else:
                if d%==0:
                    return(b,d)
               	else:
                    return(b)
        else:
            if c%2==0:
                if d%==0:
                    return(c,d)
               	else:
                    return(c)
           	else:
                if d%==0:
                    return(d)
               	else:
                    return()