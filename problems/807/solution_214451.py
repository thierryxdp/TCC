def conta_frases(texto):
    '''Dado um texto, a função retorna o número de frases contidas no mesmo.
    sendo os separadores pontuações quaisquer: exclamação, reticências etc.;
    str -> int'''
     x = str.replace(texto,'...','H')
   
    return str.count(x,'.') + str.count(x,'!') + str.count(x, '?') str.count(x,'H')