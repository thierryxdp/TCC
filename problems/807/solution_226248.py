def conta_frases (frase):
    '''
    str -> int
    '''
    return int(int(frase.count('.'))+int(frase.count('!'))+int(frase.count('?')+int(frase.count('...')))