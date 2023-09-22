def conta_frases(frase):
    '''função que conta o número de frases'''
    x=str.index(frase,'.',0,-1)
    y=str.index(frase,'!',0,-1)
    z=str.index(frase,'?',0,-1)
    w=str.index(frase,"...",0,-1)
    total= x+y+z+w	
    return total