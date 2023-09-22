def conta_frases(texto):
    str.replace(texto,'! ','. ')
    str.replace(texto,'? ','. ')
    str.replace(texto,'...','.')
    x = str.split(texto,'.')
    return len(x)