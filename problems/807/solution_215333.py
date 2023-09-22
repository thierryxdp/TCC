def conta_frases(texto):
    '''A funcao conta o numero de frases
      determinado texto; 
      str -> int'''
    pntfinal=(texto,'.')
    pntexclamacao=(texto,'!')
    pntinterrogacao=(texto,'?')
    reticencias=(texto,'...')
    return pntfinal + pntexclamacao + pntinterrogacao + reticencias