def filtra_pares(x):
    if x[0]%2==0:
        if x[1]%2==0:
            if x[2]%2==0:
                if x[3]%2==0:
                    return (x[0],x[1],x[2],x[3])
                else:
                    return (x[0],x[1],x[2])
            elif x[3]%2==0:
                return (x[0],x[1],x[3])
            else:
                return (x[0],x[1])
        elif x[2]%2==0:
            if x[3]%==0:
                return (x[0],x[2],x[3])
            else:
                return (x[0],x[2])
    elif x[1]%2==0:
            if x[2]%2==0:
                if x[3]%2==0:
                    return (x[1],x[2],x[3])
                else:
                    return (x[1],x[2])
            elif x[3]%2==0:
                return (x[1],x[3])
            else:
                return (x[1])
    elif x[2]%2==0:
        if x[3]%2==0:
            return (x[2],x[3])
        else:
            return (x[2])
    elif x[3]%2==0:
                return (x[3])
    elif x[0]%2==0: 
        return (x[0])
    else:
        return ()