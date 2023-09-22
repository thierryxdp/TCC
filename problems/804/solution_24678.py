def filtra_pares(x,y,z,w):
    if (x/2!=int(x/2)):
        return (y,z,w)
    elif (y/2!=int(y/2)):
        return (x,z,w)
    elif (z/2!=int(z/2)):
        return (x,y,w)
    elif (w/2!=(w/2)):
        return (x,y,z)
    else:
        return (x,y,z,w)