def conta_frases(frase):
    frase1 = str.count(frase,'!')
    frase2 = str.count(frase,'.')
    frase3 = str.count(frase,'?')
    frase4 = str.count(frase,'...')
    if '!' in frase:
        return frase1
    elif '.' in frase:
        return frase2
    elif '?' in frase:
        return frase3
    elif '...' in frase:
        return frase4
    else:
        return frase1+frase2+frase3+frase4