def filtra_pares(a,b,c,d):
        if a%2==0 and b%2==0 and c%2==0 and d%2==0:
                return (a,b,c,d)
        else:
                if a%2!=0 and b%2==0 and c%2==0 and d%2==0:
                        return (b,c,d)
                else:
                        if a%2==0 and b%2!=0 and c%2==0 and d%2==0:
                                return (a,c,d)
                        else:
                                if a%2==0 and b%2==0 and c%2!=0 and d%2==0:
                                        return (a,b,d)
                                else:
                                        if a%2==0 and b%2==0 and c%2==0 and d%2!=0:
                                                return(a,b,c)