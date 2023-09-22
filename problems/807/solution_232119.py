def conta_frases(texto):
    """conta o numero de frases que aparece no texto
    as frases se distinguem depois de ponto final,exclamação,
    interrogaçao ou reticencias
    str->int"""
    tira1 = str.count(texto,'.')
    tira2 = str.count(texto,'!')
    tira3 = str.count(texto,'...')
    tira4 = str.count(texto,'?')-3*tira3
    frase = tira1 + tira2 + tira3 + tira4
    return frase