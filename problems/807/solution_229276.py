def conta_frases(frases):
    '''Retorna o número de frases'''
    numpf=str.count(frases,'.')
    numinter=str.count(frases,'?')
    numret=str.count(frases,'...')
    numexc=str.count(frases,'!')
    return numpf+numinter+numret+numexc