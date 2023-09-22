def posLetra(x,y,z):
    if x.count(y) == 0 :
        return -1
    else:
        return x.count(y) + z