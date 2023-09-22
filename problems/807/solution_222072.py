def conta_frases (frase):
    w = frase.split('?')
    x = frase.split('!')
    y = frase.split('.')
    z = frase.split('...')
    return len(w)+len(x)+len(y)+len(z)