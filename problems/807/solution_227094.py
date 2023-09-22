def conta_frases(frases):
    '''função que conta o número de frases que contem um texto'''
    'str -> int'
    novafrase = str.replace(frases,'...','.')

    if  ('.') in frases:
        return novafrase.count('.')
    elif ('?') in frases:
        return frases.count('?')
    elif ('.') and ('!') in frases:
        return frases.count('.','!')