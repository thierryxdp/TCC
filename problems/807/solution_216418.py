def conta_frases(frase):
    ret = '...'
    ponfinal = '.'
    x = frase.split(ponfinal)
    y = frase.split(ret)
    z = frase.split('!')
    a = frase.split('?')
    return len(x)+len(y)+len(z)+len(a)