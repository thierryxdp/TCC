def posLetra(x,y,z):
    if x.count(y) == 0 :
        return -1
    elif x.count(y) - z == 0:
        return 0
    else:
        return x.count(y) + z