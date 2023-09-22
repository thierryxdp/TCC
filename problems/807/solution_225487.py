def conta_frases(frase):
    frase = str.replace(frase,'.','...')
    return str.count(frase,'...')+str.count(frase,'!')+str.count(frase,'?')