def conta_frases(texto):
    '''Função que conta as frases existentes em um texto;
    str -> int'''
    
    x = str.count(str.split(texto,'!'))
    y = str.count(str.split(texto,'.'))
    z = str.count(str.split(texto,'?'))
    
    return x + y + z