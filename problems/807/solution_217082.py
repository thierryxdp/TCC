def conta_frases(s):
    ''' Função que retorna o numero de frases em texto;str->int'''
    numReticencias=s.count('...')
    numPontoFinal=s.count('.')-3*numReticencias
    return numReticencias+numPontoFinal+s.count('!')+s.count('?')