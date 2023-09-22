def conta_frases(texto):
    ''' Essa função conta o número de frases que aparecem no texto.
    Cada frase no texto é terminada com um ponto final,um posto de exclamação
    , um ponto de interrogação ou três pontos.str-->str'''
    return (len(texto.split('.')) - 2*texto.count('...')) + len(texto.split('!') )+ len(texto.split('?'))-3