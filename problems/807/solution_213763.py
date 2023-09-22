def conta_frases(frase):
    x = str.split(frase,'.')
    a = str.split(x,'!')
    b = str.split(a,'?')
    c = str.split(b,'...')
    y = str.join('#',c)
    return y.count('#')