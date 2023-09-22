def conta_frases(K):
	pontos         = K.count('.') - 3*(K.count)
    excl           = K.count('!')
    interr         = K.count('?')
    retic          = K.count('...')
    
    return excl+interr+retic+pontos