def posLetra(x,y,z):
    
    if z <= 1:
        posicao = x.find(y)
        return posicao
    elif z > 1:
        return -1