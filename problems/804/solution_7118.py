def filtra_pares(M):
    """filtra uma tupla e devolve só elementos pares"""
    if M[0]%2==0 and M[1]%2==0 and M[2]%2==0 and(M[3]%2==0):
        return (a,b,c,d)
    else:
        if M[0]%2==0 and M[1]%2==0 and M[2]%2==0 and not(M[3]%2==0):
            return (a,b,c)
        else:
            if M[0]%2==0 and M[1]%2==0 and not(M[2]%2==0)and not(M[3]%2==0):
                return (a,b)
            else:
                if a%2==0 and not(b%2==0) and not(c%2==0)and not(d%2==0):
                    return (a)
                else:
                    if not(a%2==0) and b%2==0 and not(c%2==0)and not(d%2==0):
                        return (b)
                    else:
                        if not(a%2==0) and not(b%2==0) and (c%2==0)and not(d%2==0):
                            return (c)
                        else:
                            if not(a%2==0) and not(b%2==0) and not(c%2==0)and(d%2==0):
                                return (d)
                            else:
                                if not(a%2==0) and not(b%2==0) and not(c%2==0)and not(d%2==0):
                                    return ()
                                else:
                                    if not(a%2==0) and not(b%2==0) and(c%2==0)and(d%2==0):
                                        return (c,d)
                                    else:
                                        if not(a%2==0) and(b%2==0) and not(c%2==0)and(d%2==0):
                                            return (b,d)
                                        else:
                                            if(a%2==0) and not(b%2==0) and not(c%2==0)and(d%2==0):
                                                return (a,d)
                                            else:
                                                if not(a%2==0) and(b%2==0) and(c%2==0)and not(d%2==0):
                                                    return (b,c)
                                                else:
                                                    if(a%2==0) and not(b%2==0) and(c%2==0)and not(d%2==0):
                                                        return (a,c)
                                                    else:
                                                        if (a%2==0) and(b%2==0) and not(c%2==0)and not(d%2==0):
                                                            return (a,b)