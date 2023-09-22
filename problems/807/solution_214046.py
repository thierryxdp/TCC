def conta_frases(frase):
    x = str.split(frase, '!')
    y = str.split(frase, '.')
    z = str.split(frase, '...')
    w = str.split(frase, '?')
    frase = x+y+z+w
    return len(frase)