def conta_frases(frase):
    a = str.partition(frase,'.')
    b = list.remove(a,'.')
    c = str.split(frase,'.')
    d = str.split(c,'!')
    return d