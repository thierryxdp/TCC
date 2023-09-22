def conta_frases(frase):
    a = str.replace(frase,'...','.')
    b = str.count(a,'.')
    c = str.count(frase,'!')
    d = str.count(frase,'?')
    total = b + c + d
    return total