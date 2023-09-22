def conta_frases(frase):
    #frase = str.strip(frase)
    frase = str.split(frase)
    frase= frase.count(frase)
    return len(frase)