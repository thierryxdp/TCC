def conta_frases(texto):
    f = str.replace(texto,'...','.')
    f1 = str.count(f,'.')
    f2 = str.count(texto,'!')
    f3 = str.count(texto,'?')
    texto = f1 + f2 + f3
    return texto