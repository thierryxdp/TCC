#asus
def conta_frases(frase):
    frase2 = frase.replace('..', ' ')
    c1 = frase2.count('.')
    c3 = frase2.count('!')
    c4 = frase2.count('?')
    #print(c1, c3, c4)
    qts_frases = c1 + c3 + c4
    return qts_frases