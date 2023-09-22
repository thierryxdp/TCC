def conta_frases(frase):
    """ função que rebeba e conte o número de frases que aparecem neste texto; str-> int"""
    x=frase
    x.count('.')
    x.count('...')
    x.count('?')
    x.count('!')
    return len(frase)