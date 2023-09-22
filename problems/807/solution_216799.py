def conta_frases(frase):
    ''' função que conta o numero de frases de um texto determinados pelas caracteres especiais ('...', '!', '?', '.' - sem repetições das mesmas)
str -> int'''
    frase = frase.replace("...",".")
    frase = frase.replace("?",".")
    frase = frase.replace("!",".")
    return frase.count(".")