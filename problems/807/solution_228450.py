def conta_frases(texto):
    '''
    '''
    
    texto=  str.split(texto,'.')
            str.split(texto,'?')
            str.split(texto,'...')
            str.split(texto,'!')
    
    return len(texto)