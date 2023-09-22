def conta_frases(texto):
    '''conta o numero de frases que aparecem no texto;
    string->tupla'''
    x = texto.count(''...'')
    y = texto.count(''.'')
    w = texto.count(''!'')
    z = texto.count(''?'')
    h = texto.count(''...'')*3
    return (x+y+w+z)-h