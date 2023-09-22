def posLetra(x,y,z):
    if x.count(y) < z :
        return -1
    elif x.count(y) > z :
        return x.count(y) + z
    else:
        return x.count(y) - z