def conta_frases(frase):
    x = frase.split('!')
    y = frase.split('.')
    z = frase.split('...')
    w = frase.split('?')
    frase = x+y+z+w
    return len(frase)