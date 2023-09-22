def filtra_pares(tupla):
    """Retorna uma tupla que contém apenas os elementos pares
    tupla(int,int,int,int) -> tupla """
    if t[0]%2!=0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0:
        return ()
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0:
        return (t[0],)
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        return (t[0],t[3])
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2!=0:    
        return (t[2],)
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:    
        return (t[0],t[2],t[3])
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        return (t[3],)
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        return (t[0],t[1],t[2],t[3])
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2==0:
        return (t[1],t[3])