def conta_frases(frases):
    x = str.count(frases,'... ')
    y = str.count(frases, '. ')
    z = str.count(frases, '?')
    w = str.count(frases, '!')
    return x + y + z + w