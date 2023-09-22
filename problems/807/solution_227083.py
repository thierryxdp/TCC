def conta_frases(frases):
    '''função que conta o número de frases que contem um texto'''
    'str -> int'

    ('...')==('$')
    
    if  ('.') in frases:
        str.replace(frases,'.','$')
        return frases.count('$')
    elif ('!') in frases:
        return frases.count('!')
    elif ('?') in frases:
        return frases.count('?')