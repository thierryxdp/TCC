def colisao (x,y):

    (a,b,c,d) = x
    (e,f,g,h) = y


    if (e>a and f>b) or (c>g and d>h):
        return False
    else:
        return True