def conta_frases(frase):
    x = str.split(frase,'.')
    x = str.split(x,'!')
    x = str.split(x,'?')
    x = str.split(x,'...')
    y = str.join('#',x)
    return y.count('#')