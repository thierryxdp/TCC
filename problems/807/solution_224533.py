def conta_frases(texto):
    '''Função que conta as frases existentes em um texto;
    str -> int'''
    
    x = len(str.split(texto,'!'))
    y = len(str.split(texto,'.'))
    z = len(str.split(texto,'?'))
    
    return x + y + z