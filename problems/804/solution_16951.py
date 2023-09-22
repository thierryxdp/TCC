def filtra_pares(t):
    """Retornar uma tupla t de quatro elementos somente com os seus elementos pares; int->int"""
    if t[0]%2 == 0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        return t
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        return(t[1],t[2],t[3],)
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:
        return(t[0],t[2],t[3],)
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2==0:
        return(t[0],t[1],t[3],)
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        return(t[0],t[1],t[2],)
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:
        return(t[2],t[3],)
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2==0:
        return(t[1],t[3],)
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0:
        return(t[1],t[3],)
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        return(t[2],t[2],)
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        return(t[0],t[3],)
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2!=0:
        return(t[0],t[2],)
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0:
        return(t[0],t[1],)
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        return(t[3],)
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2!=0:
        return(t[2],)
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0:
        return(t[1],)
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0:
        return(t[0],)
    else:
        return()