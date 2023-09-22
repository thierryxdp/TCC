b=t[1]
c=t[2]
d=t[3]
if a%2==0:
    if b%2==0:
        if c%2==0:
            if d%2==0:
                return (a,b,c,d)
            else:
                return (a,b,d)
            else:
                return (a,b)
            else:
                if c%2==0:
                    if d%2==0:
                        return (a,d)
                    else:
                        return (a,)
                    else:
                        if b%2==0:
                            if c%2==0:
                                if d%2==0:
                                    return (b,c,d)
                                else:
                                    return (b,c)
                                else:
                                    if d%2==0:
                                        return (b,d)
                                    else:
                                        return (b,)
                                    else:
                                        if c%2==0: