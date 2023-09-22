def conta_frases(frase):
    """ função que receba e conte o número de frases que aparecem neste texto; str-> int"""
    r=0
    x=frase
    r= r+x.count('.')
    r= r+x.count('...')
    r= r+x.count('?')
    r= r+x.count('!')
    return r