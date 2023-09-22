def filtra_pares(tupla):
    '''Filtra os numeros pares de uma tupla
    	int,int,int,int-> Os numeros pares int'''
    tuple(x,y,z,w)=tupla
    if (x%2==0,y%2==0,z%2==0,w%2==0):
        return (x,y,z,w)
    elif (x%2==0,y%2==0,z%2==0,w%2!=0):
        return (x,y,z)
    elif (x%2==0,y%2==0,z%2!=0,w%2!=0):
        return (x,y)
    elif (x%2==0,y%2!=0,z%2!=0,w%2!=0):
        return (x)
    elif (x%2==0,y%2!=0,z%2==0,w%2==0):
        return (x,z,w)
    elif (x%2==0,y%2!=0,z%2==0,w%2!=0):
        return (x,z)
    elif (x%2==0,y%2!=0,z%2!=0,w%2==0):
        return (x,w)
    elif (x%2==0,y%2==0,z%2!=0,w%2==0):
        return (x,y,w)
    elif (x%2!=0,y%2==0,z%2==0,w%2==0):
        return (y,z,w)
    elif (x%2!=0,y%2==0,z%2==0,w%2!=0):
        return (y,z)
    elif (x%2!=0,y%2!=0,z%2==0,w%2==0):
        return (y,w)
    elif (x%2!=0,y%2!=0,z%2==0,w%2==0):
        return (z,w)
    elif (x%2!=0,y%2!=0,z%2!=0,w%2==0):
        return (w)
    elif (x%2!=0,y%2!=0,z%2==0,w%2!=0):
        return (z)
    elif (x%2!=0,y%2==0,z%2!=0,w%2!=0):
        return (y)
    else:
        return()