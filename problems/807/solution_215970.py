def conta_frases(frase):
    frase1 = str.count(frase,'!')
    frase2 = str.count(frase,'.')
    frase3 = str.count(frase,'?')
    frase4 = str.count(frase,'...')
    frasef = frase1+frase2+frase3+frase4
    if frase1 == True and frase2 == True and frase3 == True and frase4 == True:
        return frasef
    elif '!' in frase:
        return frase1
    elif '.' in frase:
        return frase2
    elif '?' in frase:
        return frase3
    elif '...' in frase:
        return frase4
    else:
        return frasef