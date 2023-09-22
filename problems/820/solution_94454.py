def posLetra(string,letra,numero):
    n=numero
    x=0
    y=0
    z=list(string).count(letra)
    while x<len(string):
        if n<z:
            return n
        
            
        elif n>z:
            return -1
        
        x=x+1