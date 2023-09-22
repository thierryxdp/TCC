def conta_frases (frase):
    '''...'''
    frase = frase.replace('...','.')
    frase = frase.replace('!','.')
    frase = frase.replace('?','.')
    frase = frase = frase.split('.')
    
    return len(frase)-1