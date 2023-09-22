def conta_frases(texto):
    '''retorna número de frases do texto
    str->int'''
    PontoNormal=str.count(texto,'.')-((str.count(texto,'...'))*3)
    PontoExclamacao=str.count(texto,'!')
    PontoInterrogacao=str.count(texto,'?')
    Reticencias=str.count(texto,'...')
    NFrases=PontoNormal+PontoExclamacao+PontoInterrogacao+Reticencias
    return NFrases