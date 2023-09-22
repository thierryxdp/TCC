def conta_frases(frase):
    '''Conta o número de frases que aparece no texto
    string -> int'''
    frases = []
    qt_ponto = frase.count('.')
    cont = 0
    if '.' in frase:
        cont += 1
        if cont < qt_ponto:
            cont += 1 - 3
    if '?' in frase:
    
        cont += 1
    if '!' in frase:
        cont += 1
    if '...' in frase:
        cont += 1
    return cont