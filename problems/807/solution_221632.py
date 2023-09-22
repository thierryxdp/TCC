def conta_frases(frase):
    b = str.partition(frase,'.')
    a = list.index(b,'.')
    del(frase[a])
    return frase