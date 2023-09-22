def colisao(k,j):
    a,b,c,d=k
    e,f,g,h=j
    if(c<e and d<f):
        return True
    elif(a<e and b<f and c>g nd d>h):
        return True
    else:
        return False