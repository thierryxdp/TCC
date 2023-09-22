def conta_frases(frase):
    a=frase.replace('...','!')
    b=a.replace('?','!')
    c=b.replace('.','!')
    return c.split('!')


def inverte(l):
    return list.reverse(conta_frases(l))