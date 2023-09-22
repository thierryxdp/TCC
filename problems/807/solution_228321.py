def conta_frases(frase):
    '''Conta o número de frases que aparece no texto
    string -> int'''
    frases = []
    ponto = frase.index('.')
    
    if '.' in frase:
        frases += [frase]
        corta = frases[::ponto]
        return corta