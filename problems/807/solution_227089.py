def conta_frases(frases):
    '''função que conta o número de frases que contem um texto'''
    'str -> int'
	str.replace(frases,'.','$')
    if  ('.') in frases:
        
        return frases.count('$')
    elif ('!') in frases:
        return frases.count('!')
    elif ('?') in frases:
        return frases.count('?')