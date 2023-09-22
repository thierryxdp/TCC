def conta_frases(texto):
    texto = str.replace(texto,'!','.')
    texto = str.replace(texto,'?','.')
    texto = str.replace(texto,'...','.')
    x = str.split(texto,'. ')
    return len(x)