def conta_frases(frases):
    '''Retorna o número de frases'''
    numpf=str.count(frases,'.')
    sempf=str.replace(frases,'.',' ')
    numinter=str.count(frases,'?')
    numret=str.count(sempf,'...')
    numexc=str.count(frases,'!')
    return numpf+numinter+numret+numexc