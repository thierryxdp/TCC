def conta_frases(texto):
    '''Essa Função conta o número de frases que aparecem 
    neste texto. Cada frase no texto  ́e terminada com um
    ponto final, um ponto de exclamação, um ponto de
    interrogação ou três pontos. str-->int'''
    return (len(texto.split('.')) - 2*texto.count('...')) + len(texto.split('!')) + len(texto.split('?'))-3