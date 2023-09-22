def conta_frases(frase):
    '''Função que conta o nmr de frases
    str->int'''
    frase = frase.replace("...",".")
    frase = frase.replace("?",".")
    frase = frase.replace("!",".")
    return frase.count(".")