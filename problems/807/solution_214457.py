def conta_frases(texto):
    '''Função que dado um texto qualquer retorna o número de frases contidas no mesmo.
    A partir de suas próprias pontuações tais como exclamação, interrogação, etc.
    str -> int'''
    x = str.replace(texto,'...','#')
    return str.count(x,'.') + str.count(x,'!') + str.count(x,'?') + str.count(x,'#')