def conta_frases(frase):
    '''função que conta o número de frases
    string -> int'''
    return len((frase.split('!') or (frase.split('.') or (frase.split('?') or frase.split('...'))