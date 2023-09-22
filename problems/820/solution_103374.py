def posLetra(x,y,z):
    inc= 0
    while inc< len(x):
        
        if str.find(x,y,z-1) < str.find(x,y,z,z):
            inc+= 1
            return -1
    
        else:
            inc+= 1
            return str.find(x,y,z-1)