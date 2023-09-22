def conta_frases(texto):
    '''Função que conta as frases existentes em um texto;
    str -> int'''
    
    texto = str.replace(texto,'...', '.')
    x = str.count(texto,'!')
    y = str.count(texto,'.')
    z = str.count(texto,'?')
    
    return x + y + z