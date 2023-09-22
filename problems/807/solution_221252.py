def conta_frases (frases):
    '''conta frase
    '''
    
    frases = str.replace(frases,'?','.')
    frases = str.replace(frases,'!','.')
    frases = str.replace(frases,'...','.')
    numero = str.count(frases,'.')
    return (numero)