def filtra_pares(w):
    """separa os números pares e apresenta em ordem"""
    if w%2==0:
        if x%2==0:
            if y%2==0:
                if z%2==0:
                    return(w,x,y,z)
                else:
                    return(w,x,y)
            else:
                if z%2==0:
                    return(w,x,z)
                else:
                    return(w,x)
        else:
            if y%2==0:
                if z%2==0:
                    return(w,y,z)
                else:
                    return(w,y)
            else:
                if z%2==0:
                    return(w,z)
                else:
                    return(w)
    else:
        if x%2==0:
            if y%2==0:
                if z%2==0:
                    return(x,y,z)
                else:
                    return(x,y)
            else:
                if z%2==0:
                    return(x,z)
                else:
                    return(x)
        else:
            if y%2==0:
                if z%2==0:
                    return(y,z)
                else:
                    return(y)
            else:
                if z%2==0:
                    return(z)
                else:
                    return()