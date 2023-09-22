def conta_frases (frase):
    '''Função que conta o nímeo de frases em um texto. str->str'''
    frase = frase.replace('...','.')
    frase = frase.replace('!','.')
    frase = frase.replace('?','.')
    frase = frase = frase.split('.')
    
    return len(frase)-1