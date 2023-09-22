def colisao(k,j):
    a,b,c,d=k
    e,f,g,h=j
    if(c<f or g<a or d<f or h<b):
        return True
    else:
        return False