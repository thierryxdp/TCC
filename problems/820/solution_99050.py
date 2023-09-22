def posLetra(string,let,y):
    x=string.find(let)
    while x>=0 and y>1:
        x=string.find(let,x+ 1)
        y=y- 1
    return y