def conta_frases(frase):
    frase = frase.replace('...','.').replace('!','.').replace('?','.')
    frase = frase.split('.')
    return len(frase)-1