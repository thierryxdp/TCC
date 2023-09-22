def conta_frases(frase):
    '''função que conta o número de frases'''
    soma=0
    if '.' in frase:
        soma+=1
    if '...' in frase:
        soma+=1
    if '?' in frase:
        soma+=1
    if '!' in frase:
        soma+=1
        return soma