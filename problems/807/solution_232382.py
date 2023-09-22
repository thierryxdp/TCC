def conta_frases(frase):
    '''função que conta o número de frases'''
    frases=0
    if '.' in frase:
        frases+=1
    if '!' in frase:
        frases+=1
    if '?' in frase:
        frases+=1
    if '...' in frase:
        frases+=1
    return frases