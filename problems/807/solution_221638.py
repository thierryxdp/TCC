def conta_frases(frase):
    a = str.partition(frase,'.')
    list.remove(a,'.')
    b = str.partition(a,'!')
    return b