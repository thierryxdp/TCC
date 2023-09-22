def conta_frases(texto):
    '''conta o numero de frases que aparecem no texto.
    string->int'''
    
    valor = texto.count(''!'') + texto.count(''?'') + texto.count(''...'') + texto.count(''.'')
    ret = texto.count(''...'')*3
    
    return valor - ret