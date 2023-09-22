def conta_frases(texto):
    '''Função que conta as frases existentes em um texto;
    str -> int'''
    
    x = str.count(texto,'!')
    y = str.count(texto,'.')
    z = str.count(texto,'?')
    r = str.count(texto,'...')
    
    return (x + y + z) - r