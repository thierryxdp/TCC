def filtra_pares(a,b,c,d):
        if a%2==0:
                if b%2==0:
                        if c%2==0:
                                if d%2==0:
                                        return (a,b,c,d)
                                
        else:
                if b%2==0:
                        if c%2==0:
                                if d%2==0:
                                        return (b,c,d)
                else:
                        if c%2==0:
                                if d%2==0:
                                        return (c,d)
                        else:
                                if d%2==0:
                                        return(d)