def conta_frases(frase):
    x=str.count(frase, '.')
    y=str.count(frase, '!')
    z=str.count(frase, '?')
    w=str.count(frase, '...')
    if w>0:
        return x+y+z+w-3*w
    else:
        return x+y+z+w