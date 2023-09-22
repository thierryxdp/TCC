def conta_frases(texto):
    texto = str.count(texto,'!')
    texto = str.count(texto,'?')
    texto = str.count(texto,'...')
    texto = str.count(texto,'.')
    return texto