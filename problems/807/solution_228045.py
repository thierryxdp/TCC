def conta_frases(frase):
    '''função que conta o numero de frases
    string -> int'''
    return frase.count((frase.split('!')) or (frase.split('?')) or (frase.split('.')) or (frase.split('...')))