def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''

    x= x()
    
    y=str.count(frase,'!',0,-1)
    x+=y
    z=str.count(frase,'.',0,-1)
    x+=z
    w=str.count(frase,'?',0,-1)
    x+=w
    v=str.count(frase,'...',0,-1)
    x+=v

    return x