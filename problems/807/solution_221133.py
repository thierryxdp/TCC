def conta_frases(texto):
    """dado um texto retorna o número de frases que o compõe
    str-->int"""
    if str.count(texto,'...')==0:
        return  str.count(texto,'?')+ str.count(texto,'.')+str.count(texto,'...')+str.count(texto,'!')
    else:
         str.count(texto,'?')+ str.count(texto,'.')+str.count(texto,'...')+str.count(texto,'!')-3*str.count(texto,'...')