def posLetra(x,y,z):
    if str.index(x,y,z-1) ==False:
        return -1
    
    else:
        return str.find(x,y,z-1)