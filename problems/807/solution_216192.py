def conta_frases (frase):
    '''...'''
    frase.replace('...','.')
    frase.replace('!','.')
    frase.replace('?','.')
    frase = frase.split('.')
    
    return len(frase)