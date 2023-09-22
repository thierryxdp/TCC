def conta_frases(frases):
    x=str.split(frases,'.')
    Y=str.split(frases,'!')
    z=str.split(frases,'?')
    v=str.split(frases,'...')
    
    return len(x)+len(y)+len(v)+len(z)-4