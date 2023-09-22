def conta_frases(frases):
    x = str.count(frases,'...')
    y = str.count(frases, '. ')
    z = str.count(frases, '?')
    w = str.count(frases, '!')
    xy = str.count(frases, '.')
    if xy == frases[-1]:
        return (x + 2y + z + w)
    else:
        return (x + y + z + w)