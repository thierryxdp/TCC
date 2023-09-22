def conta_frases(frase):
    x = str.split(frase,'.')
    y = str.split(x,'!')
    return len(y)