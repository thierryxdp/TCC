def conta_frases(frases):
    x=frases.split('?')
    y=frases.split('.')
    z=frases.split(!) 
    w=frases.split('...')
    return len(x+y+z+w)