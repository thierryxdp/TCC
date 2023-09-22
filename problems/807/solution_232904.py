def conta_frases(texto):
    '''Retorna a quantidade de frases presentes no texto; str -> int'''
    frases=str.count(texto, '.')
    frases=frases+str.count(texto, '?')
    frases=frases+str.count(texto, '!')
    return frases