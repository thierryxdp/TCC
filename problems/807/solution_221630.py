def conta_frases(frase):
    b = str.partition(frase,'.')
    a = list.index(frase,b)
    del(frase[a])
    return frase