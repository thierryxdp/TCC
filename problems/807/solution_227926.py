def conta_frases(frase):
    frase2=frase.replace('...','.')
    if frase :
        return frase2
   
     elif frase:
        return frase2.count('.')  + frase2count('!') +frase2.count('?')