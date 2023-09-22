def conta_frases(frase):
    frase1 = str.partition(frase,'.')
    frase2 = str.partition(frase,'...')
    frase3 = str.partition(frase,'!')
    frase4 = str.partition(frase, '?')
    if frase1 == True:
    if frase2 == True:
    if frase3 == True:
    if frase4 == True:
    return len(frase1+frase2+frase3+frase4)