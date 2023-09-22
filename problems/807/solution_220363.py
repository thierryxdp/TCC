def conta_frases(frase):
    '''Retorna o número de frases de um texto
    string -> int '''
    frase=frase.replace('...','?')
    frase=frase.replace('!','?')
    frase=frase.replace('?','?')
    frase=frase.replace('.','?')
    return frase.count('?')