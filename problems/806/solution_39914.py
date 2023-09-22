def colisao (x,y):

    (a,b,c,d) = x
    (e,f,g,h) = y


    if (e>c and (f>d or h<b))or (a>g and (b>h or d<f)) or (c<e and (b>g or d<f)):
        
        return False
    
    else:
        return True