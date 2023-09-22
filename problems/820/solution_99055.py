def posLetra(string,letra,y):
    x=string.find(letra)
    while x >=0 and y>1:
        x=string.find(letra,x+ 1)
        y=y- 1
    return x