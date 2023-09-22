def conta_frases(texto):
    l=texto.split('.')
    b=str.join(' ',l)
    l=b.split('!')
    b=str.join(l)
    l=b.split('?')
    b=str.join(l)
    l=b.split('...')
    c=len(l)
    return c