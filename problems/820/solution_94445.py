def posLetra(string,letra,numero):
    n=numero
    x=0
    y=0
    z=list(string).count(letra)
    while x<len(string):
        if n<z:
            a=list(string).index(letra)
            if a==0:
                return a+1
            return a*n
            
        elif n>z:
            return -1
        
        x=x+1
    return y