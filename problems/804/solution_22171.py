def par(x):
    return x%2


def filtra_pares(tupa):
    x=tupa[0]
    y=tupa[1]
    z=tupa[2]
    w=tupa[3]
    if par(x)==0:
        return x,
    else:
        return ()
    if par(y)==0:
        return (y,)
    elif par(x)!=0:
        return (y,)
    elif par(y)!=0:
        return (x,)