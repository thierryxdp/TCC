def posLetra(a,b,c):
    inc= 0
    while inc< len(a):
        
        if str.find(a,b,c-1) < str.find(a,b,c,c):
            inc+= 1
            return -1
        
        if str.count(a,b) < str.find(c):
          
            return '-1'
    
        else:
            inc+= 1
            return str.find(a,b,c-1)