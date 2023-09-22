def conta_frases(frases):
    x = str.count(frases,'...')
    y = str.count(frases, '.')
    z = str.count(frases, '?')
    w = str.count(frases, '!')
    xy = str.count(frases, '. ')
    if y== frases[-1]:
        return x + y + z + w + xy
    else:
        return (x + y + z + w)