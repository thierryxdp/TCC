def conta_frases(frase):
    '''Dada um texto, retorna quantas frases há no texto.'''
    frase = frase.replace('...','.')
    return str.count(frase,'?') + str.count(frase,'!') + str.count(frase,'...') + str.count(frase,'.')