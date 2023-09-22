def filtra_pares(a,b,c,d):
    '''retorna uma tupla com apenas os números pares dentre a, b, c e d'''
    if(type(a/2)==int):
        if(type(b/2)==int):
            if(type(c/2)==int):
                if(type(d/2)==int):
                    return (a,b,c,d)
                else:
                    return (a,b,c)
            elif(type(d/2)==int):
                return (a,b,d)
            else:
                return (a,b)
        elif(type(c/2)==int):
            if(type(d/2)==int):
                    return (a,c,d)
                else:
                    return (a,c)
        elif(type(d/2)==int):
            return (a,d)
        else:
            return (a,)
    elif(type(b/2)==int):
        if(type(c/2)==int):
            if(type(d/2)==int):
                return (b,c,d)
            else:
                return (b,c)
        elif(type(d/2)==int):
            return (b,d)
        else:
            return (b,)
    elif(type(c/2)==int):
        if(type(d/2)==int):
            return (c,d)
        else:
            return (c,)
    elif(type(d/2)==int):
        return (d,)
    else:
        return(,)