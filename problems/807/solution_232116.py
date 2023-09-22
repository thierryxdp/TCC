def conta_frases(texto):
    """conta o numero de frases que aparece no texto
    as frases se distinguem depois de ponto final,exclamação,
    interrogaçao ou reticencias
    str->int"""
    tira1 = str.replace(texto,'.','')
    tira2 = str.replace(texto,'!','')
    tira3 = str.replace(texto,'...','')
    tira4 = str.replace(texto,'?','')
    frase = (tira1 + tira2 + tira3 + tira4)
    len frase