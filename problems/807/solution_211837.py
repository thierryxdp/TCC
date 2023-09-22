def conta_frases(frase):
    if frase['...']:
        return frase.count('...') + frase.count('!') + frase.count('?') + frase.count('. ')
    else:
        return frase.count('...') + frase.count('!') + frase.count('?') + frase.count('.')