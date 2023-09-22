def posLetra(a,b,c):
    inc= 0
    num = str.count(a,b)
    while inc< len(a):
        
        
        
        if num < str.find(c):
          
            return -1
    
        else:
            inc+= 1
            return str.find(a,b,c-1)