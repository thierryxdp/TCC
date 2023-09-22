def colisao(k,j):
    a,b,c,d=k
    e,f,g,h=j
    if(c<e or g<a or d<f or h<a):
        return True
    else:
        return False