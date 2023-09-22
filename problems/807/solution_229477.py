def conta_frases(frase):
    frase = a
    a = str.split(a,'!')
    a = str.join('.',a)
    a = str.split(a,'?')
    a = str.join('.',a)
    a = str.split(a,'...')
    a = str.join('.',a)
    a = str.split(a,'.')
    n_frases = len(a) - 1
    return n_frases