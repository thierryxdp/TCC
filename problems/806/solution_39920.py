def colisao(x,y):

    (a,b,c,d) = x
    (e,f,g,h) = y

    if e>c or f>d or a>g or h<b:
        return False

    else:
        return True