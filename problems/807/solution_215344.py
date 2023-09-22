def conta_frases(texto):
    '''A funcao conta o numero de frases
      determinado texto; 
      str -> int'''
    pntfinal=str.count(texto,'.')
    pntexclamacao=str.count(texto,'!')
    pntinterrogacao=str.count(texto,'?')
    reticencias=str.count(texto,'...')
    if int(reticencias) >0:
        return  pntexclamacao + pntinterrogacao + reticencias + pntfinal - 3(reticencias)
    else:    
        return pntfinal + pntexclamacao + pntinterrogacao + reticencias