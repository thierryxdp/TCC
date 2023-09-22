def conta_frases(frases):
    '''Retorna o número de frases'''
    numret=str.count(frases,'...')
    semret=str.replace(frases,'...',' ')
    numexc=str.count(frases,'!')
    numpf=str.count(semret,'.')
    numint=str.count(semret,'?')
    return numret+numexc+numpf+numint