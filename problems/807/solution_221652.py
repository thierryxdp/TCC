def conta_frases(frase):
    if '.' in frase:
    a = str.count(frase, '.')
    str.replace(frase,'.','',a)
    return frase