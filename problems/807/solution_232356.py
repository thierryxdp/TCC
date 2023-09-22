def conta_frases(frase):
    '''função que conta o número de frases'''
    x=str.index(frase,'.',0,)
    y=str.index(frase,'!',0,)
    z=str.index(frase,'?',0,)
    w=str.index(frase,'...',0,)
    total= x+y+z+w	
    return total