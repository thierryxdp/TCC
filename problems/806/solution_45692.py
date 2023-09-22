def colisao(k,j):
    a,b,c,d=k
    e,f,g,h=j
    if(a<g and b<h and c<e and d<f):
        return True
    else:
        return False