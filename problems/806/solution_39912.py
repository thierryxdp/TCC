def colisao (x,y):

    (a,b,c,d) = x
    (e,f,g,h) = y


    if (e>c and f>b) or (a>g and d>h):
        
        return False
    
    else:
        return True