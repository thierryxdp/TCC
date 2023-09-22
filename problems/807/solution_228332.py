def conta_frases(frase):
    '''Conta o número de frases que aparece no texto
    string -> int'''
    frases = []
    ponto = frase.index('.')
    interrgocao = frase.index('?')
    cont = 0
    if '.' in frase:
        corta = frase[:ponto]
        cont += 1
    if '?' in frase:
        corta = frase[:interrogacao]
        return corta