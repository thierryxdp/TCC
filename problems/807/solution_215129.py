def conta_frases(frase):
    s=frase.count('!')
    t=frase.count('?')
    w=frase.count('...')
    y=frase.count('.')
    return s+t-2*w+y