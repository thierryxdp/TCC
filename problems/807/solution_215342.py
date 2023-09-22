def conta_frases(texto):
    '''A funcao conta o numero de frases
      determinado texto; 
      str -> int'''
    pntfinal=str.count(texto,'.')
    pntexclamacao=str.count(texto,'!')
    pntinterrogacao=str.count(texto,'?')
    reticencias=str.count(texto,'...')
    if reticencias >0:
        return  pntexclamacao + pntinterrogacao + reticencias + pntfinal - 3(reticiencias)
    else:    
        return pntfinal + pntexclamacao + pntinterrogacao + reticencias