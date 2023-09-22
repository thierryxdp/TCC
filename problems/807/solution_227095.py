def conta_frases(frases):
    '''função que conta o número de frases que contem um texto'''
    'str -> int'
    novafrase1 = str.replace(frases,'...','.')
    novafrase2 = str.replace(frases,'!','.')

    if  ('.') in frases:
        return novafrase1.count('.')
    elif ('!') and ('.')in frases:
        return novafrase2.count('.')
    elif ('!') in frases:
        return frases.count('!')
    elif ('?') in frases:

        return frases.count('?')
    elif ('.') and ('!') in frases:
        return novafrase2.count('.')