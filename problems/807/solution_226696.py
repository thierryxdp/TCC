def conta_frases(frases):
    '''função que conta o número de frases que contem um texto'''
    'str - int'

    
    if  ('.') or '!' or '?' in frases:
        return frases.count('.')+frases.count('!')+frases.count('?')
    elif ('...') or '!' or '?' or '.' in frases:
        return  frases.count('.')+ frases.count('.') + frases.count('!')+frases.count('?')