def conta_frases(frase):
    x=str.count(texto, '.')
    y=str.count(texto, '!')
    z=str.count(texto, '?')
    w=str.count(texto, '...')
    if w>0:
        return x+y+z+w-3*w
    else:
        return x+y+z+w