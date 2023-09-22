def conta_frases(frase):
    frase = str.split(frase,'.') and str.split(frase,'!') and str.split(frase,'?') and str.split(frase,'...')
    return len(frase)