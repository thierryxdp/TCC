def conta_frases(frase):
    frase1 = str.split(frase,'.')
    frase2 = str.split(str.split(frase,'.'),'?')
    return len(frase2)