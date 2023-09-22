def conta_frases(texto):
    nReticencias= str.count(texto,'...')
    nPontoFinal= str.count(texto, '.') - 3*nReticencias
    return nReticencias + nPontoFinal + str.count(texto, '!') + str.count(texto, '?')