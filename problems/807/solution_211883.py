def conta_frases(texto):
    '''Dado um texto, retorna o número de frases;
    Sendo frases terminadas com pontos de exclamação, interrogação, reticencias ou ponto final;
    str => int'''
    def x1(texto):
        return str.count(str.rstrip(str.lstrip(texto)),'?')
    def x2(texto):
        return str.count(str.rstrip(str.lstrip(texto)),'!')
    def x3(texto):
        return str.count(str.rstrip(str.lstrip(texto)),'.')
    def x4(texto):
        return str.count(str.rstrip(str.lstrip(texto)),'...')
    if int(str.find(texto,'...')==-1):
        return int(x1(texto))+int(x2(texto))+int(x3(texto))
    elif not int(str.count(texto,'...'))==1:
        return int(x1(texto))+int(x2(texto))+int(x3(texto))-4
    else:
        return int(x1(texto))+int(x2(texto))+int(x3(texto))+int(x4(texto))-3