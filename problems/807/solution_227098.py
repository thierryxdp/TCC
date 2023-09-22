def conta_frases(frases):
    '''função que conta o número de frases que contem um texto'''
    'str -> int'
    novafrase1 = str.replace(frases,'...','.')
    novafrase2 = str.replace(novafrase1,'!','.')
    novafrase3 = str.replace(novafrase2,'?','.')

    if  ('.') in frases and not ('!')in frases and not ('?') in frases:
        return novafrase1.count('.')
    elif ('!') in frases and ('.')in frases and not ('?') in frases:
        return novafrase2.count('.')
    elif ('.') in frases and ('?') in frases and not ('!') in frases:
        return novafrase3.count('.')