def posLetra(x,y,z):
    if str.find(x,y,z) < str.find(x,y,z,z):
        return -1
    
    
    else:
        return str.find(x,y,z)