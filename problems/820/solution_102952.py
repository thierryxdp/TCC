def posLetra(x,y,z):
    if z< str.find(x,y):
        return -1
    else:
        return str.find(x,y,z)