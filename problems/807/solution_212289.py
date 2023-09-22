def conta_frases(frase):
    '''Dada um texto em string, retorna quantas frases há no texto.
     str -> int'''
    s = frase 
    return str.count(s, '?') + str.count(s, '.') + str.count(s, ''...'') + str.count(s, '!')