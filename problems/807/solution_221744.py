def conta_frases(frases):
    x=frases.split('?')
    y=frases.split('.')
    w=frases.split('...')
    z=frases.split(!) 
    return len(x+y+z+w)