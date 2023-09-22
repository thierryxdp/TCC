def conta_frases(texto):
    '''
    '''
    
    texto= str.split(texto,'.')
    texto1=str.split(texto,'?')
    texto2=str.split(texto,'...')
    texto3=str.split(texto,'!')
    
    return len(texto+texto1+texto2+texto3)