def posLetra(string,letra,numero):
    n=numero
    x=0
    y=0
    z=list(string).count(letra)
    while x<len(string):
        if n<z:
            return x=x+1
            
        elif n>z:
            return -1
        
        x=x+1