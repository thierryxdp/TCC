def conta_frases(frase):
    p = str.count(frase,'.')
    e = str.count(frase, '!')
    i = str.count(frase,'?')
    r = str.count(frase,'...')
    return p*-3r + e + i + r