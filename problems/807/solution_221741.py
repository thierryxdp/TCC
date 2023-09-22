def conta_frases(frase):
    frase = str.replace('!','.')
    return len(str.split(frase))