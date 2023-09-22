def conta_frases(texto):
    '''Dado um texto, a função retorna o número de frases contidas no mesmo.
    sendo os separadores pontuações quaisquer: exclamação, reticências etc.;
    str -> int'''
    str.replace(texto,'...','H')
    return str.count(texto,'.') + str.count(texto,'!') + str.count(texto, '?') str.count(texto,'H')