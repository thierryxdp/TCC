def posLetra(string,letra,numero):
    s=[]
    x=0
    while x<len(string):
        if letra in string:
            s=s+list(string[x].index(letra))
        else:
            s
        x=x+1
    return s