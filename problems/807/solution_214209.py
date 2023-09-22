def conta_frases(frase):
    x = str.count(frase, '.')
    y = str.count(frase, '...')
    z = str.count(frase, '!')
    w = str.count(frase, '?')
    x = x - y*3
    return x+y+z+w