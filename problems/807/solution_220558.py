def conta_frases (frase):
    x = str.replace(frase, ('!'), '.')
    y = str.replace(x, ('...'), '.')
    z = str.replace(y, ('?'), '.')
 
    return frase.strchr(".")