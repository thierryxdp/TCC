def conta_frases(frase):
    a=frase.split('.')
    b=a.split('?')
    c=b.split('!')
    d=c.split('...')
    return len(d)