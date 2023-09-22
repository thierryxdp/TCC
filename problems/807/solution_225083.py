import string
def conta_frases(frase):
    a=frase.replace('...','!')
    b=a.replace('?','!')
    c=b.replace('.','!')
    return len(c.split('!'))-1