def conta_frases(texto):
    '''Função que conta as frases existentes em um texto;
    str -> int'''
    
    x = len(texto.split(texto,'!'))
    y = len(texto.split(texto,'.'))
    z = len(texto.split(texto,'?'))
    
    return x + y + z