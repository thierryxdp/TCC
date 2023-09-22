def conta_frases(frase):
    frase=frase.replace('...','.')
    
    if frase:
        return frase.count('.')  + frase.count('!') +frase.count('?')