def conta_frases(frases):
    '''função que conta o número de frases que contem um texto'''
    'str - int'
    if  ('...') in frases:
        
        frases.count('...')==frases.count('.')-frases.count('..')
        return frases.count('!') + frases.count('?')+ frases.count('...')
    else:
        return frases.count('!') + frases.count('?')+ frases.count('.')