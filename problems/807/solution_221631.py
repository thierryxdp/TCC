def conta_frases(frase):
    b = str.partition(frase,'.')
    a = list.index(frase,'.')
    del(frase[a])
    return frase