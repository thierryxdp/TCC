def conta_frases(frase):
    if '...' in frase:
        return frase.count('.')+frase.count('...')+frase.count('?')+frase.count('!')-3*frase.count('...')
    else:
        return frase.count('.')+frase.count('?')+frase.count('!')