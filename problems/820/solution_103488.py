def posLetra(a,b,c):
    inc= 0
    num=str.count(a,b)
    if str.count(a,b) < (c):
            inc+= 1
            return -1
    while inc< len(a):
        
        if str.find(a,b,c-1) < str.find(a,b,c,c):
            inc+= 1
            return -1
        

    
        else:
            inc+= 1
            return str.find(a,b,c-1)