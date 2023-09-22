def conta_frases(frase):
    frase1 = str.split(frase,'.')
    if '.' in frase==True:
        return len(frase1)